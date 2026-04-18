# Konu: Bankamatik Uygulaması (Basit)
# Amaç: Fonksiyonlar ve sözlükler kullanarak basit bir banka hesabı yönetimi (para çekme, bakiye sorgulama).

OguzHesap = {
    'ad': 'Oguz Akgül',
    'hesapNo': '123123123',
    'bakiye': 3000,
    'ekHesap': 2000,
}
BoraHesap = {
    'ad': 'Bora Caba',
    'hesapNo': '1231231234',
    'bakiye': 3000,
    'ekHesap': 2000,
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}"),
    
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsınmı (e/h)')

            if ekHesapKullanimi == 'e':
                bakiye = hesap['bakiye']
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar

                print('paranizi alabilirisiniz')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır.")
        else:
            print("bakiyeniz yetersiz")


def bakiyeSorgula (hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']}tl bulunmaktadır.")
paraCek(OguzHesap, 3000)
bakiyeSorgula(OguzHesap)
paraCek(OguzHesap, 2000)

    
# �ZET: Fonksiyonlar ve s�zl�kleri birle�tirerek, temel para �ekme mant���na ve ek hesap kullan�m�na sahip basit bir bankamatik sim�lasyonu yap�yoruz.
