from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# FastAPI uygulamasının ana giriş noktası
# Burada uygulamayı başlatacağız ve gerekli middleware (güvenlik, loglama vb.) ayarlarını yapacağız.
app = FastAPI(title="SentinelAI: Sahtekarlık Tespit Sistemi")

# --- VERİ MODELLERİ (SCHEMAS) ---
# Pydantic kullanarak gelen finansal işlem verilerinin tip kontrolünü yapacağız.
# Örneğin: tutar (float), kullanıcı_id (str) gibi zorunlu alanlar burada tanımlanacak.

# --- ENDPOINT TANIMLARI ---
# 1. Root (/): Sistemin ayakta olup olmadığını kontrol eden basit bir selamlama ucu.
# 2. Predict (/predict): Bir finansal işlemi alıp "Fraud" (sahte) olup olmadığını söyleyen ana fonksiyon.
# 3. History (/transactions): Veritabanına kaydedilen geçmiş işlemleri listeleyen uç.

if __name__ == "__main__":
    # Uygulamayı geliştirme modunda çalıştırmak için uvicorn ayarları
    pass
