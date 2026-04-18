# W01: Değişkenler & Veri Tipleri - Özet
# ========================================

# 1. DEĞİŞKEN OLUŞTURMA
name = "Oğuz"
age = 21
is_student = True
print(f"{name} is {age} years old. Student: {is_student}")

# 2. TİP DÖNÜŞÜMÜ
# str -> int/float
number_str = "123"
number_int = int(number_str)
number_float = float("123.45")

# int -> str
age_str = str(age)

print(f"Converted: {number_int}, {number_float}, {age_str}")

# 3. VERİ TİPLERİ
# int, float, str, bool
integer = 42
floating = 3.14
string = "Hello"
boolean = False

# type() fonksiyonu
print(type(integer))  # <class 'int'>
print(type(floating))  # <class 'float'>

# 4. RANDOM MODÜLÜ
import random

# Rastgele tam sayı
dice = random.randint(1, 6)
print(f"Dice roll: {dice}")

# Rastgele seçim
colors = ["red", "blue", "green"]
chosen = random.choice(colors)
print(f"Random color: {chosen}")

# Rastgele ondalık sayı
random_num = random.random()  # 0.0 ile 1.0 arası
print(f"Random float: {random_num}")

# 5. SAYI TAHMİN OYUNU (Mini Örnek)
secret = random.randint(1, 10)
print("Guess a number between 1 and 10!")
# guess = int(input("Your guess: "))
# if guess == secret:
#     print("Correct!")
# else:
#     print(f"Wrong! It was {secret}")
