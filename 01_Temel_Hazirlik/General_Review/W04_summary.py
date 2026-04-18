# W04: Koleksiyonlar (List, Tuple, Set, Dict) - Özet
# ====================================================

# 1. LİSTELER (Değiştirilebilir, Sıralı)
numbers = [1, 2, 3, 4, 5]
numbers.append(6)       # Sona ekle
numbers.insert(0, 0)    # Belirli indekse ekle
numbers.remove(3)       # Değeri kaldır
numbers.pop()           # Son elemanı kaldır
numbers.sort()          # Sırala
numbers.reverse()       # Ters çevir

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 2. TUPLE'LAR (Değiştirilemez, Sıralı)
coordinates = (10, 20)
x, y = coordinates  # Unpacking (açma)

# Tuple'lar değiştirilemez
# coordinates[0] = 15  # HATA!

# 3. SET'LER (Değiştirilebilir, Sırasız, Benzersiz)
unique_nums = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
unique_nums.add(5)
unique_nums.remove(2)

# Set işlemleri
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Birleşim: {1, 2, 3, 4, 5}
print(set1 & set2)  # Kesişim: {3}
print(set1 - set2)  # Fark: {1, 2}

# 4. SÖZLÜKLER (Anahtar-Değer Çiftleri)
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

# Erişim
print(student["name"])      # Ali
print(student.get("age"))   # 20

# Ekleme/Güncelleme
student["city"] = "Istanbul"
student["age"] = 21

# Metotlar
print(student.keys())    # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values())  # dict_values(['Ali', 21, 'A', 'Istanbul'])
print(student.items())   # Anahtar-değer çiftleri

# 5. ÖZET TABLO
# Tip       | Değiştirilebilir | Sıralı | Tekrar | Sözdizimi
# --------- | ---------------- | ------ | ------ | ---------
# List      | Evet             | Evet   | Evet   | []
# Tuple     | Hayır            | Evet   | Evet   | ()
# Set       | Evet             | Hayır  | Hayır  | {}
# Dict      | Evet             | Evet*  | Key:No | {k:v}
