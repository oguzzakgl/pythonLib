# W03: Koşullar & Operatörler - Özet
# =========================================

# 1. KOŞULLU İFADELER (if-elif-else)
age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 2. BOOLEAN VERİ TİPİ
is_active = True
is_admin = False

print(type(is_active))  # <class 'bool'>

# 3. KARŞILAŞTIRMA OPERATÖRLERİ
x = 10
y = 20

print(x == y)  # False (eşit)
print(x != y)  # True (eşit değil)
print(x < y)   # True (küçük)
print(x > y)   # False (büyük)
print(x <= y)  # True (küçük veya eşit)
print(x >= y)  # False (büyük veya eşit)

# 4. MANTIKSAL OPERATÖRLER
a = True
b = False

print(a and b)  # False (ikisi de True olmalı)
print(a or b)   # True (en az biri True)
print(not a)    # False (tersi)

# 5. ARİTMETİK OPERATÖRLER
num1 = 10
num2 = 3

print(num1 + num2)  # 13 (toplama)
print(num1 - num2)  # 7 (çıkarma)
print(num1 * num2)  # 30 (çarpma)
print(num1 / num2)  # 3.333... (bölme)
print(num1 // num2) # 3 (tam bölme)
print(num1 % num2)  # 1 (mod/kalan)
print(num1 ** num2) # 1000 (üs)

# 6. ATAMA OPERATÖRLERİ
count = 5
count += 3  # count = count + 3 -> 8
count -= 2  # count = count - 2 -> 6
count *= 2  # count = count * 2 -> 12
count //= 4 # count = count // 4 -> 3

# 7. ÜYELİK OPERATÖRLERİ
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)      # True
print("grape" not in fruits)  # True

# 8. BİTSEL OPERATÖRLER (İleri Seviye)
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
print(5 & 3)   # 1 (ikili AND)
print(5 | 3)   # 7 (ikili OR)
