
bakiye = 1000 

while True:
    print("\n--- ATM'ye Hoşgeldiniz ---")
    print("Lütfen yapmak istediğiniz işlemi seçiniz.")
    print("1. Bakiye Sorgula")
    print("2. Para Yatır")
    print("3. Para Çek")
    print("4. Çıkış")
    
    secim_str = input("İşlem (1-4): ")


    if not secim_str.isdigit():
        print("Lütfen sadece sayı (1-4) giriniz.")
        continue 


    islem = int(secim_str)


    if islem == 1:
        print(f"Güncel bakiyeniz: {bakiye} TL")

        
    elif islem == 2:
        print(f"Mevcut Bakiyeniz: {bakiye} TL")
        yatirilan_para = int(input("Yatırmak istediğiniz tutarı giriniz: "))
        

        bakiye += yatirilan_para 
        
        print(f"Para yatırma başarılı. Yeni bakiyeniz: {bakiye} TL")

        
    elif islem == 3:
        print(f"Mevcut Bakiyeniz: {bakiye} TL")
        

        cekilen_para = int(input("Çekmek istediğiniz tutarı giriniz: "))
        

        if cekilen_para > bakiye:
            print(f"Yetersiz bakiye! En fazla {bakiye} TL çekebilirsiniz.")
        else:

            bakiye -= cekilen_para 
            print(f"Para çekme başarılı. Kalan bakiyeniz: {bakiye} TL")



    elif islem == 4:
        print("Çıkış yapılıyor. İyi günler dileriz.")
        break 
        
    else:
        print("Geçersiz işlem. Lütfen 1-4 arasında bir seçim yapınız.")
# �ZET: 'while' d�ng�s� ve ko�ullu ifadeler kullanarak; bakiye sorgulama, para yat�rma ve �ekme i�lemlerini sim�le eden temel bir ATM uygulamas� kurguluyoruz.
