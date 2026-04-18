# W08: Modüller - Özet
# =====================

# 1. MATH MODÜLÜ
import math

print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045
print(math.sqrt(16))     # 4.0
print(math.factorial(5)) # 120
print(math.ceil(4.2))    # 5 (yukarı yuvarla)
print(math.floor(4.8))   # 4 (aşağı yuvarla)
print(math.pow(2, 3))    # 8.0 (2^3)

# Trigonometri
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0

# 2. DATETIME MODÜLÜ
from datetime import datetime, timedelta, date

# Şu anki tarih ve saat
now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Belirli bir tarih oluştur
birthday = datetime(2004, 5, 17)
print(birthday)

# Tarih aritmetiği
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(tomorrow)

# Tarih farkı
diff = now - birthday
print(f"Doğum gününden bu yana geçen gün: {diff.days}")

# 3. RANDOM MODÜLÜ
import random

# Rastgele tam sayı
dice = random.randint(1, 6)
print(f"Zar: {dice}")

# Rastgele seçim
colors = ["red", "blue", "green"]
print(random.choice(colors))

# Rastgele karıştır
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

# Rastgele ondalık
print(random.random())  # 0.0 ile 1.0 arası

# 4. STATISTICS MODÜLÜ
import statistics

data = [10, 20, 30, 40, 50]
print(statistics.mean(data))    # 30.0 (ortalama)
print(statistics.median(data))  # 30 (ortanca değer)
print(statistics.stdev(data))   # Standart sapma

# 5. PLATFORM MODÜLÜ
import platform

print(platform.system())         # Windows/Linux/Darwin
print(platform.python_version()) # 3.x.x

# 6. ÖZEL MODÜL OLUŞTURMA
# Dosya: my_module.py
# def greet(name):
#     return f"Hello, {name}!"
# 
# PI = 3.14159

# Özel modülü kullanma:
# import my_module
# print(my_module.greet("Ali"))
# print(my_module.PI)

# Veya:
# from my_module import greet, PI
# print(greet("Ali"))
# print(PI)

# 7. IMPORT ÇEŞİTLERİ
# import math              # Tüm modülü içe aktar
# from math import sqrt    # Belirli fonksiyonu içe aktar
# from math import *       # Her şeyi içe aktar (önerilmez)
# import math as m         # Takma ad ile içe aktar
# from math import sqrt as square_root  # Fonksiyon takma adı
