# SayÄ± Tahmin Oyunu (Basit)
import random

random_sayi = random.randint(1,100)
tahmin_hakki = 5

print("SayÄ± tahmin oyununa hoÅŸ geldiniz.")

while (tahmin_hakki>0):
    tahmin = int(input("Lutfen 1 ile 100 arasÄ±nda bir sayÄ± giriniz: "))
    tahmin_hakki -=1
    if tahmin < 1 or tahmin > 100:
        print("Lutfen 1 ile 100 arasÄ±nda bir sayÄ± giriniz")
        continue
    if tahmin == random_sayi:
        print (f"Tebrikler {tahmin_hakki} denemede doÄŸru bildiniz.")
        break
    elif tahmin < random_sayi:
        print ("Daha bÃ¼yÃ¼k bir sayÄ± giriniz")
    elif tahmin > random_sayi:
        print ("Daha kÃ¼cÃ¼k bir sayi giriniz")
else:
    print ("Tahmin hakkÄ±nÄ±z bitti.")
        
# ÖZET: 'random' kütüphanesi ve 'while' döngüsü kullanarak; kullanıcının bilgisayarın tuttuğu sayıyı 5 hak içerisinde bulmaya çalıştığı temel bir tahmin oyunu kurguluyoruz.
