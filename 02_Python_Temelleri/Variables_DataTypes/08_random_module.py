import random

print(random.random())  # 0.0 ile 1.0 arasında rastgele bir ondalık sayı üretir

# seed ile rastgele sayı üreteciyi başlatma
random.seed(10)  # Rastgele sayı üreteciyi sabit bir başlangıç değeri ile başlatır
print(random.random())
random.seed(10)  # Aynı başlangıç değeri ile tekrar başlatılır
print(random.random())  # Aynı rastgele sayı üretilir

# state ile rastgele sayı üreteci durumunu kaydetme ve geri yükleme
print(random.random()) # Yeni bir rastgele sayı üretir
state= random.getstate()  # Mevcut durumu al
print(random.random()) # Yeni bir rastgele sayı üretir
random.setstate(state)  # Önceki duruma geri dön
print(random.random())  # Aynı rastgele sayı üretilir


# randrange ile belirli bir aralıkta rastgele tam sayı üretme (baslangic , bitis , adim)
print(random.randrange(1, 10))  # 1 ile 9 arasında rastgele bir tam sayı üretir
# adım değeri ile kullanımı 
print(random.randrange(0, 10, 2))  # 0 ile 9 arasında çift sayılardan rastgele bir tam sayı üretir
# negatif aralıkta kullanımı
print(random.randrange(-10, -1))  # -10 ile -2 arasında rastgele bir tam sayı üretir
# tek sayılar arasında kullanımı
print(random.randrange(1, 10, 2))  # 1 ile 9 arasında tek sayılardan rastgele bir tam sayı üretir
# tek sayılar arasında negatif adım ile kullanımı
print(random.randrange(10, 1, -2))  # 10 ile 2 arasında tek sayılardan rastgele bir tam sayı üretir

# ÖZET: Python'da rastgele sayı üretimi için kullanılan 'random' modülünün temel fonksiyonlarını ve üreteç durumunu kontrol etmeyi öğreniyoruz.
