# Stok Kontrol Sistemi (Dictionary Yapısı)
envanter = {
    "TLF01": {"ad": "S23 Ultra", "stok": 50, "fiyat": 3000},
    "KLV01": {"ad": "F108 Pro", "stok": 40, "fiyat": 1200}
}

print("Stok kontrol sistemine hoş geldiniz!")
while True:
    print("\nMENU")
    print("1: Ürün Ekle / Güncelle")
    print("2: Ürünü Envanterden Sil")
    print("3: Envanteri Listele")
    print("4: Toplam Envanter Değerini Göster")
    print("5: Çıkış")
    secim = input("Bir seçenek girin (1-5): ").strip()

    if secim == "1":
        kod = input("Ürün kodunu girin: ").strip().upper()
        try:
            ad = input("Ürün adını girin: ")
            stok = int(input("Stok miktarını girin: "))
            fiyat = float(input("Ürün fiyatını girin: "))
        except ValueError:
            print("Geçersiz giriş. Lütfen tekrar deneyin.")
            continue

        envanter[kod] = {"ad": ad, "stok": stok, "fiyat": fiyat}
        print(f"{ad} envantere eklendi/güncellendi.")

    elif secim == "2":
        if not envanter:
            print("Silinecek ürün yok, envanter boş.")
            continue

        print("\n--- Envanter Listesi (Silmek için kod seçin) ---")
        for k, b in envanter.items():
            print(f"Kod: {k}, Ad: {b['ad']}, Stok: {b['stok']}, Fiyat: {b['fiyat']} TL")
        print("------------------------------------------------")
        kod = input("Silinecek ürün kodunu girin: ").strip().upper()

        kayit = envanter.pop(kod, None)
        if kayit is not None:
            print(f"{kod} kodlu ürün envanterden silindi.")
        else:
            print("Ürün bulunamadı.")

    elif secim == "3":
        if not envanter:
            print("Envanter boş.")
            continue
        print("Envanter Listesi:")
        for k, b in envanter.items():
            print(f"Kod: {k}, Ad: {b['ad']}, Stok: {b['stok']}, Fiyat: {b['fiyat']} TL")

    elif secim == "4":
        toplam_deger = sum(b['stok'] * b['fiyat'] for b in envanter.values())
        print(f"Toplam envanter değeri: {toplam_deger} TL")

    elif secim == "5":
        print("Çıkış yapılıyor. İyi günler!")
        break

    else:
        print("Geçersiz seçenek.")

# �ZET: S�zl�k yap�lar�n� i� i�e (nested) kullanarak; �r�nlerin kodlar�na g�re stok miktarlar�n� ve fiyatlar�n� y�neten, toplam envanter de�erini hesaplayan profesyonel bir takip sistemi olu�turuyoruz.
