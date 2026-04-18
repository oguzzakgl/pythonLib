# W10: İleri Düzey Python - Özet
# ================================

# 1. LIST COMPREHENSIONS
# Geleneksel yol
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension (modern)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Koşul ile
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# İç içe
matrix = [[i*j for j in range(3)] for i in range(3)]

# 2. GENERATORS & YIELD
def countdown(n):
    while n > 0:
        yield n  # Duraklat ve değer döndür
        n -= 1

# Generator bellekte liste oluşturmaz
for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1

# Generator ifadesi (list comprehension gibi ama () ile)
gen = (x**2 for x in range(1000000))  # Bellek dostu!

# 3. DECORATORS (Dekoratörler)
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Süre: {end - start:.4f}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Tamamlandı"

# slow_function()  # Otomatik olarak zamanlanır

# 4. TYPE HINTING (Tip İpuçları)
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}"

# Koleksiyonlar için tip ipuçları
from typing import List, Dict, Tuple

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# 5. ASYNC/AWAIT (Asenkron Programlama)
import asyncio

async def fetch_data(id: int):
    print(f"{id} getiriliyor...")
    await asyncio.sleep(1)  # Ağ gecikmesini simüle et
    return f"Data {id}"

async def main():
    # Birden fazla görevi eşzamanlı çalıştır
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)

# asyncio.run(main())  # Async kodu çalıştır

# 6. CONTEXT MANAGERS (with)
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# with FileManager('test.txt') as f:
#     f.write('Hello')

# 7. SİHİRLİ METOTLAR (Magic Methods)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Vector(4, 6)

# 8. REGEX (Düzenli İfadeler)
import re

text = "E-postam test@example.com"
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
if match:
    print(match.group())  # test@example.com

# Tüm eşleşmeleri bul
emails = re.findall(r'\w+@\w+\.\w+', "a@b.com, c@d.org")
print(emails)  # ['a@b.com', 'c@d.org']

# 9. JSON
import json

# Python'dan JSON'a
data = {"name": "Ali", "age": 25}
json_string = json.dumps(data, indent=2)

# JSON'dan Python'a
parsed = json.loads(json_string)

# Dosya işlemleri
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=2)

# 10. REQUESTS (HTTP)
# import requests
# 
# response = requests.get('https://api.github.com')
# print(response.status_code)  # 200
# print(response.json())       # JSON yanıtını ayrıştır
