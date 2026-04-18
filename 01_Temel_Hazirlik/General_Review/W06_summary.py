# W06: Fonksiyonlar - Özet
# =========================

# 1. TEMEL FONKSİYON
def greet():
    print("Hello!")

greet()  # Fonksiyonu çağır

# 2. PARAMETRELİ FONKSİYON
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ali")

# 3. DEĞER DÖNDÜREN FONKSİYON
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# 4. VARSAYILAN PARAMETRELER
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# 5. *args (Değişken Sayıda Argüman)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# 6. **kwargs (Anahtar Kelime Argümanları)
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Ali", age=20, city="Istanbul")

# 7. GLOBAL vs YEREL DEĞİŞKENLER
global_var = "Ben globalim"

def test_scope():
    local_var = "Ben lokalim"
    print(global_var)  # Global'e erişebilir
    print(local_var)   # Local'e erişebilir

test_scope()
# print(local_var)  # HATA! Fonksiyon dışında erişilemez

# Global değişkeni değiştirme
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# 8. LAMBDA FONKSİYONLARI (İsimsiz)
# Normal fonksiyon
def square(x):
    return x ** 2

# Lambda eşdeğeri
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# Lambda ile map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda ile filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 9. DOCSTRING
def calculate_area(radius):
    """
    Bir dairenin alanını hesaplar.
    
    Args:
        radius: Dairenin yarıçapı
        
    Returns:
        Dairenin alanı
    """
    return 3.14 * radius ** 2

print(calculate_area.__doc__)  # Docstring'i yazdır
