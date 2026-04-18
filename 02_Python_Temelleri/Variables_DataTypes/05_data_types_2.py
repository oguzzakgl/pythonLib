# Python Programlamada Tür Belirleme ve Dönüştürme
# ------------------------------------------------

# type() fonksiyonu ile tür belirleme
sayi = 25
metin = "25"
ondalik = 25.0
dogru_mu = True

print(type(sayi))
print(type(metin))
print(type(ondalik))
print(type(dogru_mu))

# int(), float(), str(), bool() dönüşümleri
# Sayıdan metine
a = 10
a_str = str(a)
print(a_str, type(a_str))

# Metinden sayıya
b = "45"
b_int = int(b)
print(b_int, type(b_int))

# Metinden ondalığa
c = "3.14"
c_float = float(c)
print(c_float, type(c_float))

# Boolean dönüşümleri
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("Python"))  # True

# 3️⃣ Karma dönüşümler
x = 5.7
y = int(x)
z = str(y)
print(x, y, z)

# 4️⃣ Hatalı dönüşüm örneği
try:
    val = int("Merhaba")
except ValueError:
    print("Hatalı dönüşüm: metin tam sayıya çevrilemez.")


# ---------------------------------

# ÖZET: Veri türü belirleme tekniklerini ve özellikle boolean (mantıksal) dönüşümlerin mantığını pekiştiriyoruz.
# - type() → değişken türünü öğrenmek için kullanılır.
# - int(), float(), str(), bool() → tür dönüşüm fonksiyonlarıdır.
# - bool("") → False, bool("Python") → True.
# - Karma dönüşümler veri temizliğinde sık kullanılır.
# - isinstance(x, int) birden fazla tür kontrolüne izin verir.
# ---------------------------------