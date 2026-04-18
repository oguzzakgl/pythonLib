print(isim, yas, sehir)

# Tip kontrolü
print(type(isim))
print(type(yas))
print(type(sehir))

# Tek satırda çoklu atama
x, y, z = 5, 10, 15
print(x, y, z)

# Aynı değeri birden fazla değişkene atama
a = b = c = "Python"
print(a, b, c)

# Dinamik tip değişimi
sayi = 10
print(sayi)
sayi = "on"
print(sayi)

# Kullanıcı girdisi örneği
ad = input("Adınızı girin: ")
print(f"Merhaba {ad}, Python değişkenlerine hoş geldin!")


# ---------------------------------

# ÖZET: Python'da değişken tanımlama kurallarını, çoklu atama yöntemlerini ve dinamik tip özelliğini öğreniyoruz.
# - Python'da değişken türü dinamik olarak atanır; tür belirtmeye gerek yoktur.
# - Aynı anda birden fazla değişken tanımlanabilir (x, y, z = 5, 10, 15).
# - Birden fazla değişkene aynı değer atanabilir (a = b = c = "Python").
# - type() fonksiyonu değişkenin türünü döndürür.
# - Değişken adları harf veya _ ile başlar; rakamla başlayamaz.
# - Büyük/küçük harf duyarlıdır: "yas" ve "Yas" farklı değişkenlerdir.
# - input() her zaman string döndürür; sayısal işlem yapılacaksa dönüşüm gerekir.
# ---------------------------------