# W05: Döngüler & Hata Yönetimi - Özet
# ======================================

# 1. WHILE DÖNGÜSÜ
count = 0
while count < 5:
    print(count)
    count += 1

# While ile break
while True:
    user_input = "exit"  # input("'exit' yazarak çıkın: ")
    if user_input == "exit":
        break

# While ile continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # 3'ü atla
    print(i)

# 2. FOR DÖNGÜSÜ
# Liste üzerinde döngü
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Range üzerinde döngü
for i in range(5):  # 0'dan 4'e
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

# 3. KOLEKSİYONLARLA DÖNGÜLER
# Liste
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)

# Sözlük
student = {"name": "Ali", "age": 20}
for key, value in student.items():
    print(f"{key}: {value}")

# 4. İÇ İÇE DÖNGÜLER
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# 5. DÖNGÜ KONTROLÜ
# break: Döngüden çık
# continue: Sonraki iterasyona geç
# pass: Hiçbir şey yapma (yer tutucu)

for i in range(10):
    if i == 5:
        break  # 5'te dur
    if i % 2 == 0:
        continue  # Çift sayıları atla
    print(i)

# 6. HATA YÖNETİMİ (try-except)
try:
    number = int("abc")  # Bu hata verecek
except ValueError:
    print("Geçersiz sayı!")

# Birden fazla hata
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Sıfıra bölünemez!")
except ValueError:
    print("Geçersiz değer!")
finally:
    print("Bu her zaman çalışır")

# 7. FAKTÖRİYEL ÖRNEĞİ
n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f"Faktöriyel: {factorial}")
