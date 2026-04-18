# Sayı Tahmin Oyunu — döngülü
# Kullanılanlar: input, print, int(), if/elif/else, while, random.randint()

import random

tutulan = random.randint(1, 100)
deneme = 0

print("1–100 arasında bir sayı tuttum. Doğru tahmine kadar devam.")

while True:
    tahmin = int(input("Tahmin: "))   # hatalı girişte program hata verir
    deneme += 1

    if tahmin < 1 or tahmin > 100:
        print("Aralık dışı. 1–100 girin.")
        continue

    if tahmin < tutulan:
        print("Daha YÜKSEK bir sayı girin.")
    elif tahmin > tutulan:
        print("Daha DÜŞÜK bir sayı girin.")
    else:
        print(f"Tebrikler! {deneme} denemede bildiniz. Doğru sayı: {tutulan}")
        break

# 🧠 NOTLAR
# - randint(1,100) üst sınır dahil değer üretir.
# - Döngü doğru tahmine kadar sürer; çıkış yok.
# - Girdi doğrulaması yok; int() hatalı metinde hata verir.

# ÖZET: Şimdiye kadar öğrendiğimiz değişken, döngü, input ve random kavramlarını birleştirerek eğlenceli bir sayı tahmin oyunu geliştiriyoruz.
