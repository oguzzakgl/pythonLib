from fastapi import FastAPI, UploadFile, File, Form  # API, Dosya Yükleme ve Form verileri için
from fastapi.middleware.cors import CORSMiddleware  # Frontend ile Backend'in konuşabilmesi için (Güvenlik)
import shutil  # Dosya kopyalama/kaydetme işlemleri için
import os  # Dosya yolları ve klasör yönetimi için
from .engine import extract_text, calculate_score, get_skills  # Kendi yazdığımız analiz fonksiyonlarını içeri alıyoruz

app = FastAPI(title="HireSync AI API")

# 1. ADIM: CORS Ayarları
# Frontend'in (HTML dosyamızın) bu API'ye erişebilmesi için gerekli izinleri veriyoruz.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. ADIM: Veri Modelleri
# İleride Pydantic kullanarak girdi ve çıktıların şemasını burada tanımlayacağız.

# 3. ADIM: Analiz Endpoint'i (/analyze)
@app.post("/analyze")
async def analyze_cv(cv: UploadFile = File(...), jd: str = Form(...)):
    """
    Bu uç nokta (endpoint), kullanıcıdan CV dosyasını ve İş İlanı metnini alır.
    """
    # 1. Gelen CV'yi geçici olarak bir klasöre kaydet.
    # 2. engine.py'deki fonksiyonu çağırıp PDF/Word'den metni oku.
    # 3. İş ilanı ile CV'yi karşılaştırıp skoru hesapla.
    # 4. Sonuçları (skor, yetenekler) frontend'e JSON olarak fırlat.
    return {"status": "success", "message": "Analiz simülasyonu çalışıyor."}

if __name__ == "__main__":
    import uvicorn
    # Uygulamayı 8000 portunda başlatıyoruz
    uvicorn.run(app, host="0.0.0.0", port=8000)
