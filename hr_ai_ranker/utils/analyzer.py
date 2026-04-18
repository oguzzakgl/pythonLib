import hashlib
import json
import re
import os
import time
import logging
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv
from utils.processor import extract_sections, clean_data, extract_contact_info

# Logger yapılandır
logger = logging.getLogger("HR-Flow-Analyzer")

# .env dosyasını ana dizinden açıkça yükle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

class GeminiClient:
    """Gemini Model yönetimi için Singleton yapısı."""
    _instance = None
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            api_key = os.getenv("GEMINI_API_KEY", "").strip()
            if not api_key:
                logger.error("❌ GEMINI_API_KEY ortam değişkeninde bulunamadı!")
                return None
            
            genai.configure(api_key=api_key)
            
            try:
                # En uygun Flash modelini dinamik seç
                models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                flash_models = [m.replace('models/', '') for m in models if 'flash' in m.lower()]
                model_name = flash_models[0] if flash_models else 'gemini-1.5-flash'
                
                cls._model = genai.GenerativeModel(model_name)
                logger.info(f"🤖 AI Modeli Hazır: {model_name}")
            except Exception as e:
                logger.error(f"⚠️ Model listeleme hatası: {e}")
                cls._model = genai.GenerativeModel('gemini-1.5-flash')
        
        return cls._model

def get_model():
    return GeminiClient.get_model()

def perform_analysis(job_desc, resume_data_list, **kwargs):
    """
    Profesyonel AI Analiz Motoru.
    """
    if not resume_data_list or not job_desc: 
        return []
    
    model = get_model()
    results = []
    
    for resume in resume_data_list:
        filename = resume.get('filename', 'Aday')
        raw_text = resume.get('raw_text', '')
        logger.info(f"🧪 Analiz ediliyor: {filename}")
        
        ai_data = None
        if model:
            try:
                prompt = f"""
                Sen kıdemli bir Teknik İK Analistisin. Verilen CV'yi iş tanımıyla (JD) derinlemesine karşılaştır.
                
                İŞ TANIMI (JD):
                {job_desc}
                
                ADAY ÖZGEÇMİŞİ:
                {raw_text}
                
                PUANLAMA KRİTERLERİ (DİNAMİK):
                1. **Teknik Uyumluluk (0-50):** İstenen diller, kütüphaneler ve araçlar söz değerinden ziyade gerçek deneyime göre puanlansın.
                2. **Proje Derinliği (0-30):** CV'deki projeler JD'deki zorluklarla ne kadar örtüşüyor? (Junior/Senior fark etmeksizin potansiyeli puanla).
                3. **Eğitim ve Sertifikalar (0-20):** İlgili bölüm okuyor/mezun olması ve sertifikalar.
                
                ÖNEMLİ: Sadece 'Kıdemli' kriterlerine bakma. Eğer aday bir öğrencisiyse ve JD'deki teknolojilerle ilgili harika projeleri varsa yüksek puan ver (%70+).
                
                İSTENEN ÇIKTI (Sadece JSON):
                {{
                  "skor": 0-100 arası toplam sayı,
                  "teknolojiler": ["Tespit edilen anahtar teknolojiler"],
                  "eksik_yetkinlikler": ["JD'de olup CV'de kesinlikle olmayanlar"],
                  "kanitlar": ["Adayı öne çıkaran 3 somut proje/deneyim yorumu"],
                  "ozet": "Kısa ve stratejik İK kararı (Neden bu skor?)",
                  "etiket": "Uzmanlık alanı (örn: Frontend, AI Engineer, Backend)",
                  "mulakat_sorulari": ["Adayın projelerine özel 3 adet derinlemesine teknik mülakat sorusu"]
                }}
                """
                
                response = model.generate_content(prompt)
                # JSON Ayıkla
                text = response.text
                if "```json" in text:
                    text = text.split("```json")[1].split("```")[0].strip()
                elif "```" in text:
                    text = text.split("```")[1].split("```")[0].strip()
                
                match = re.search(r'\{.*\}', text, re.DOTALL)
                if match:
                    ai_data = json.loads(match.group())
                else:
                    ai_data = json.loads(text.strip())
                
                logger.info(f"✅ AI Analizi Başarılı: {filename} (Skor: {ai_data.get('skor')})")
            except Exception as e:
                logger.warning(f"⚠️ AI Analiz hatası ({filename}): {e}")
                ai_data = None

        # --- FALLBACK (AI Başarısızlığı Durumu) ---
        if not ai_data:
            logger.info(f"🔄 Fallback çalışıyor: {filename}")
            jd_words = set(re.findall(r'\w+', job_desc.lower()))
            cv_words = set(re.findall(r'\w+', raw_text.lower()))
            common = jd_words.intersection(cv_words)
            tech_match = [w for w in common if len(w) > 3]
            
            ai_data = {
                "skor": min(len(tech_match) * 6, 85),
                "teknolojiler": tech_match[:10],
                "eksik_yetkinlikler": ["Bağlantı sorunu nedeniyle AI tam liste çıkaramadı."],
                "kanitlar": ["Metin eşleşmesi üzerinden başarı puanı verildi.", "Gelişmiş analiz modu geçici olarak kapalı."],
                "ozet": "Anahtar kelime bazlı temel eşleşme sağlandı.",
                "etiket": "Hızlı Tarama",
                "mulakat_sorulari": [f"{tech_match[0] if tech_match else 'Yazılım'} tecrübenizi anlatır mısınız?"]
            }

        # Veri modelini hazırla
        sections = extract_sections(raw_text)
        results.append({
            'Aday': filename,
            'Skor': ai_data.get('skor', 0),
            'Semantik_Skor': ai_data.get('skor', 0),
            'Eşleşen_Yetkinlikler': ai_data.get('teknolojiler', []),
            'Eksik_Yetkinlikler': ai_data.get('eksik_yetkinlikler', []),
            'Bolum_Skorlari': {sec: ai_data.get('skor', 0) for sec in sections},
            'Bolum_Detaylari': {sec: content[:100] + "..." for sec, content in sections.items()},
            'Kanitlar': ai_data.get('kanitlar', []),
            'Iletisim': extract_contact_info(raw_text),
            'Etiket': ai_data.get('etiket', 'Genel'),
            'Ozet': ai_data.get('ozet', ''),
            'Mülakat_Soruları': ai_data.get('mulakat_sorulari', []),
            'Anahtar_Kelime_Skor': len(ai_data.get('teknolojiler', [])) * 5
        })
        
        if model: time.sleep(1.5) # RPM Kısıtlaması

    results.sort(key=lambda x: x['Skor'], reverse=True)
    return results
