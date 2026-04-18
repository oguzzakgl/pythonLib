import sys
import os
import logging
import shutil
import asyncio
import json
import pandas as pd
import io
from datetime import datetime
from typing import List
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

# Proje kök dizinini sisteme ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.reader import extract_text_auto
from utils.processor import clean_data
from utils.analyzer import perform_analysis, get_model
from backend.models import AnalysisResponse, EmailRequest, EmailResponse, ChatRequest, ChatResponse
import google.generativeai as genai

# Logging Yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("HR-Flow-API")

# .env yükle
load_dotenv()

app = FastAPI(title="HR-Flow AI API", version="3.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 HR-Flow AI API başlatılıyor...")
    key = os.getenv("GEMINI_API_KEY", "")
    if key:
        logger.info(f"🔑 Gemini API Anahtarı aktif: {key[:5]}...{key[-4:]}")
    else:
        logger.error("❌ KRİTİK HATA: GEMINI_API_KEY bulunamadı!")
    
    # Modelin hazır olduğundan emin ol
    try:
        get_model()
        logger.info("✅ AI Modeli başarıyla yüklendi.")
    except Exception as e:
        logger.error(f"❌ AI Modeli yükleme hatası: {e}")

@app.get("/")
async def root():
    return {
        "status": "online", 
        "version": "3.0",
        "timestamp": datetime.now().isoformat()
    }

TEMP_DIR = os.path.join(os.environ.get('TEMP', '/tmp'), "hr_flow_resumes")
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_resumes(
    job_description: str = Form(...),
    files: List[UploadFile] = File(...),
):
    logger.info(f"📥 Yeni analiz isteği: {len(files)} dosya")
    resumes_for_analysis = []
    
    try:
        # 1. Dosyaları Oku ve Metin Çıkar (Paralel Değil - Dosya Sistemi Güvenliği İçin)
        for file in files:
            file_path = os.path.join(TEMP_DIR, file.filename)
            try:
                with open(file_path, "wb") as buffer:
                    shutil.copyfileobj(file.file, buffer)
                
                # Asenkron okuma (Bloklamayı önlemek için thread'e taşıyoruz)
                raw_text = await asyncio.to_thread(extract_text_auto, file_path)
                
                if not raw_text:
                    logger.warning(f"⚠️ {file.filename} içeriği okunamadı.")
                    continue
                
                logger.info(f"📄 Okundu: {file.filename} ({len(raw_text)} karakter)")
                resumes_for_analysis.append({
                    'filename': file.filename,
                    'clean_text': clean_data(raw_text),
                    'raw_text': raw_text
                })
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

        if not resumes_for_analysis:
            logger.error("❌ Hiçbir CV'den metin çıkarılamadı.")
            raise HTTPException(status_code=400, detail="CV dosyaları okunamadı veya format desteklenmiyor.")

        # 2. Analiz (Async Wrapper Kullanılabilir ama analyzer senkron sleep içeriyor)
        # Şimdilik ana döngüyü bloklamamak için basitçe çalıştırıyoruz
        logger.info(f"⚙️ {len(resumes_for_analysis)} aday için derin analiz başlıyor...")
        results = perform_analysis(job_description, resumes_for_analysis)
        
        logger.info(f"✅ Analiz başarıyla tamamlandı. {len(results)} aday işlendi.")
        return {"results": results, "job_description": job_description}

    except Exception as e:
        logger.exception("❌ Analiz sırasında beklenmedik hata!")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/export")
async def export_to_excel(req: AnalysisResponse):
    try:
        logger.info(f"📊 Excel raporu oluşturuluyor ({len(req.results)} aday)")
        
        # Veriyi DataFrame'e dönüştür
        data = []
        for r in req.results:
            data.append({
                "Aday": r.Aday,
                "Skor (%)": r.Skor,
                "Etiket": r.Etiket,
                "İK Özeti": r.Ozet,
                "Teknolojiler": ", ".join(r.Eşleşen_Yetkinlikler),
                "Eksik Yetkinlikler": ", ".join(r.Eksik_Yetkinlikler or []),
                "Kanıtlar": " | ".join(r.Kanitlar),
                "Mülakat Soruları": " | ".join(r.Mülakat_Soruları),
                "Email": r.Iletisim.emails[0] if r.Iletisim.emails else "",
                "Telefon": r.Iletisim.phones[0] if r.Iletisim.phones else ""
            })
            
        df = pd.DataFrame(data)
        
        # Excel dosyasını bellekte (memory) oluştur
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Analiz Raporu')
            
            # Sütun genişliklerini ayarla
            worksheet = writer.sheets['Analiz Raporu']
            for i, col in enumerate(df.columns):
                column_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.column_dimensions[chr(65 + i)].width = min(column_len, 50)

        output.seek(0)
        
        filename = f"HR_Flow_Analiz_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        logger.error(f"❌ Excel export hatası: {e}")
        raise HTTPException(status_code=500, detail=f"Excel oluşturulamadı: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
async def chat_with_hr_assistant(req: ChatRequest):
    try:
        model = get_model()
        if not model:
            return {"reply": "AI servisi şu an kullanılamıyor.", "filtered_candidates": None}

        # Aday özetlerini kısıtla (Token limit)
        candidates_summary = [{
            "name": c.Aday,
            "score": c.Skor,
            "skills": c.Eşleşen_Yetkinlikler[:5],
            "label": c.Etiket
        } for c in req.results[:10]] # İlk 10 aday

        prompt = f"""
        Uzman İK Asistanı olarak yanıtla. 
        İŞ TANIMI: {req.job_description}
        ADAYLAR: {json.dumps(candidates_summary, ensure_ascii=False)}
        SORU: {req.message}
        
        Sadece JSON döndür: {{"reply": "...", "filtered_candidates": ["Aday.pdf", ...]}}
        """

        response = model.generate_content(prompt)
        text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)

    except Exception as e:
        logger.error(f"❌ Chat hatası: {e}")
        return {"reply": "Mesajınızı şu an işleyemiyorum.", "filtered_candidates": None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.api:app", host="0.0.0.0", port=8000, reload=True)
