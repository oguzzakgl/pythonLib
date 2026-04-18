# SayÄ± Tahmin Oyunu (PuanlÄ±)
import random

sayi = random.randint(1, 100)
puan = 100
hak = 10

print ("SayÄ± tahmin oyununa hoÅŸ geldiniz!")
print ("1 ile 100 arasÄ±nda bir sayÄ± tuttum. Bu sayÄ±yÄ± bilmek iÃ§in 10 hakkÄ±nÄ±z var.")

while hak > 0:
    tahmin = int(input("Tahmininizi giriniz: "))
    hak -= 1
    if tahmin < 1 or tahmin > 100:
        print("LÃ¼tfen 1 ile 100 arasÄ±nda bir sayÄ± giriniz.")
        continue
    if tahmin == sayi:
        print(f"Tebrikler! {10 - hak} denemede doÄŸru bildiniz. PuanÄ±nÄ±z: {puan}")
        break
    elif tahmin < sayi:
        print("Daha bÃ¼yÃ¼k bir sayÄ± giriniz.")
        puan -= 10
    else:
        print("Daha kÃ¼Ã§Ã¼k bir sayÄ± giriniz.")
        puan -= 10
else:
    print(f"Tahmin hakkÄ±nÄ±z bitti. DoÄŸru sayÄ± {sayi} idi.")

# ÖZET: Sayı tahmin oyununa puanlama sistemi ve daha fazla deneme hakkı ekleyerek; algoritma mantığını oyunlaştırma (gamification) unsurlarıyla nasıl geliştirebileceğimizi görüyoruz.
