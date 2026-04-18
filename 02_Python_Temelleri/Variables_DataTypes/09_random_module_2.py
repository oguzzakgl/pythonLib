import random

# randint ile belirli bir aralıkta rastgele tam sayı üretme (başlangıç, bitiş)
print(random.randint(1, 10))  # 1 ile 10 arasında rastgele bir tam sayı üretir
print(random.randint(-10, -1))  # -10 ile -1 arasında rastgele bir tam sayı üretir

# choice ile bir diziden rastgele eleman seçme
liste = ['elma', 'muz', 'çilek', 'portakal']
print(random.choice(liste))  # listedeki rastgele bir meyve seçer
text = "Python"
print(random.choice(text))  # metindeki rastgele bir karakter seçer

# shuffle ile bir diziyi karıştırma
dizi = [1, 2, 3, 4, 5]
random.shuffle(dizi)  # diziyi rastgele karıştırır
print(dizi)

# sample ile bir diziden belirli sayıda rastgele eleman seçme
dizi2 = [10, 20, 30, 40, 50]
print(random.sample(dizi2, 3))  # diziden 3 rastgele eleman seçer

# ÖZET: Liste içerisinden rastgele seçim yapma, karıştırma ve örnekleme gibi ileri seviye 'random' işlemlerini keşfediyoruz.
