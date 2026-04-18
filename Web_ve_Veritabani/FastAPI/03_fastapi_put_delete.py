# KONU: FastAPI ile Veri Güncelleme (PUT) ve Silme (DELETE)
# Amaç: CRUD döngüsünü tamamlamak (Create, Read, Update, Delete).

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# SAHTE VERİTABANI
kullanici_db = [
    {"id": 1, "isim": "Ahmet", "soyisim": "Yılmaz", "sifre": "1234"},
    {"id": 2, "isim": "Ayşe", "soyisim": "Demir", "sifre": "abcd"},
]

class KullaniciUpdate(BaseModel):
    isim: str
    soyisim: str
    sifre: str

@app.get("/kullanicilar")
async def kullanicilari_getir():
    return kullanici_db

# ---------------------------------------------------------
# 1. VERİ GÜNCELLEME (PUT)
# ---------------------------------------------------------
# Mantık: Hangi ID güncellenecek? Yeni veriler ne?
@app.put("/kullanici-guncelle/{kullanici_id}")
async def kullanici_guncelle(kullanici_id: int, yeni_veri: KullaniciUpdate):
    # 1. Kullanıcıyı bul
    for kullanici in kullanici_db:
        if kullanici["id"] == kullanici_id:
            # 2. Verileri değiştir
            kullanici["isim"] = yeni_veri.isim
            kullanici["soyisim"] = yeni_veri.soyisim
            kullanici["sifre"] = yeni_veri.sifre
            return {"mesaj": "Veri güncellendi!", "guncel_hal": kullanici}
    
    # 3. Bulunamazsa HATA ver (404 Not Found)
    raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı!")

# ---------------------------------------------------------
# 2. VERİ SİLME (DELETE)
# ---------------------------------------------------------
# Mantık: Hangi ID silinecek?
@app.delete("/kullanici-sil/{kullanici_id}")
async def kullanici_sil(kullanici_id: int):
    for kullanici in kullanici_db:
        if kullanici["id"] == kullanici_id:
            kullanici_db.remove(kullanici)
            return {"mesaj": "Kullanıcı başarıyla silindi.", "silinen_id": kullanici_id}
            
    raise HTTPException(status_code=404, detail="Silinecek kullanıcı yok!")

# Çalıştırmak için:
# uvicorn 03_fastapi_put_delete:app --reload

# �ZET: Bir API'nin temel i�levleri olan CRUD d�ng�s�n� tamamlamak i�in; mevcut verileri g�ncellemeyi (PUT) ve sistemden silmeyi (DELETE) pratik ediyoruz.
