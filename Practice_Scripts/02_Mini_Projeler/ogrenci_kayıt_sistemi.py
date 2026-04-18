ogrenciler = []
print("Öğrenci Kayıt Sistemine Hoş Geldiniz!")

while True:
    # Menü seçenekleri
    print("\n--- ANA MENÜ ---")
    print("1: Yeni Öğrenci Ekle")
    print("2: Tüm Öğrencileri Listele")
    print("3: Öğrenci sil")
    print("Q: Çıkış")

    # Seçim al
    secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")

    # İşlem yap
    
    if secim == '1':
        # Öğrenci Ekle
        

        isim = input("Ogrenci ismini giriniz: ") 

        soyisim = input("Ogrenci soyismini giriniz: ")
        numara = input("Ogrenci numarasını giriniz: ")
        
        yeni_ogrenci = {
            'isim': isim,
            'soyisim': soyisim,
            'numara': numara
        }
        ogrenciler.append(yeni_ogrenci)
        print(f"{isim} {soyisim} başarıyla kaydedildi!")

    elif secim == '2':

        print("\nKayıtlı Öğrenciler:")
        for ogrenci in ogrenciler:
            print(f"{ogrenci['numara']}: {ogrenci['isim']} {ogrenci['soyisim']}")

    elif secim == '3':
        numara_sil = input("Silmek istediğiniz öğrencinin numarasını giriniz: ")
        for ogrenci in ogrenciler:
            if ogrenci['numara'] == numara_sil:
                ogrenciler.remove(ogrenci)
                print(f"{ogrenci['isim']} {ogrenci['soyisim']} başarıyla silindi!")
                break
        else:
            print("Numara bulunamadı.")
    elif secim.lower() == 'q':
        # Çıkış
        print("Sistemden çıkılıyor...")
        break # Döngüyü sonlandır
        
    else:
        # Hatalı seçim
        print("Geçersiz seçim yaptınız, lütfen tekrar deneyin.")

# Çıkış mesajı
print("İyi günler!")
# �ZET: Kullan�c�dan al�nan verilerle yeni kay�tlar olu�turan, bunlar� bir listede saklayan ve istenildi�inde belirli ��rencileri silen pratik bir kay�t otomasyonu yap�yoruz.
