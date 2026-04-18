# Stok Takip ve Analiz UygulamasÄ± - Ana ModÃ¼l
import database 

while True:
    print("1- Ekle")
    print("2- Listele")
    print("3- Ã‡Ä±kÄ±ÅŸ")
    secim = input("SeÃ§im: ")
    if secim == "1":
        ad = input("Ad: ")
        fiyat = float(input("Fiyat: "))
        stok = int(input("Stok: "))
        database.urun_ekle(ad, fiyat, stok)
    elif secim == "2":
        urunler = database.urunleri_getir()
        print("\n--- ÃœRÃœN LÄ°STESÄ° ---")
        for urun in urunler:
            print(f"ID: {urun[0]}, Ad: {urun[1]}, Fiyat: {urun[2]}, Stok: {urun[3]}")
    elif secim == "3":
        break
# ÖZET: Stok takip sisteminin kullanıcı arayüzü katmanı olarak; veritabanı işlemlerini çağıran ve kullanıcı seçimlerine göre program akışını yöneten ana modülü kurguluyoruz.
