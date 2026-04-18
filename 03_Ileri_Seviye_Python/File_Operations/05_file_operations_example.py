# Konu: Dosya İşlemleri Örneği (İkramiye Kayıt)
# Amaç: Kullanıcıdan alınan verileri dosyaya ekleme (append) ve okuma (read) uygulaması.

def ikramiyeGir():
    ad = input("Lutfen ad giriniz: ")
    soyad = input("Lutfen soyad giriniz: ")
    yazİkramiye = input("Lutfen yaz ikramiyesini giriniz: ")
    kisİkramiye = input("Lutfen kıs ikramiyesini giriniz: ")
    
    with open("ikramiyeler.txt", "a", encoding="utf-8") as file:
        file.write(f"{ad} {soyad} = {yazİkramiye} + {kisİkramiye}\n")

    print("İkramiye başarıyla girildi.")

def ikramiyeListele():
    with open("ikramiyeler.txt", "r", encoding="utf-8") as file:
        icerik = file.read()
        print(icerik)


while True:
    print("\n***** MENU *****")
    print("1- İkramiye gir")
    print("2- İkramiye listele")
    print("3- Çıkış")
    
    secim = input("Seçiminiz: ")

    if secim == "1":
        ikramiyeGir()
    elif secim == "2":
        ikramiyeListele()        
    elif secim == "3":
        break
# �ZET: Dosya okuma ve yazma i�lemlerini birle�tirerek; kullan�c�dan al�nan ikramiye bilgilerini bir metin dosyas�na kaydeden ve geri listeleyen pratik bir uygulama geli�tiriyoruz.
