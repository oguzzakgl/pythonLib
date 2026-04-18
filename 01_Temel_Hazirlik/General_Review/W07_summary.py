# W07: Nesne Yönelimli Programlama (OOP) - Özet
# ===============================================

# 1. SINIF & NESNE TEMELLERİ
class Person:
    # Sınıf niteliği (tüm örnekler tarafından paylaşılır)
    species = "Human"
    
    # Yapıcı metot
    def __init__(self, name, age):
        # Örnek nitelikleri (her nesneye özgü)
        self.name = name
        self.age = age
    
    # Örnek metot
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")

# Nesneler oluştur
person1 = Person("Ali", 25)
person2 = Person("Ayşe", 30)

person1.introduce()  # Hi, I'm Ali, 25 years old
print(Person.species)  # Human

# 2. KALITIM (Inheritance)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Üst sınıf yapıcısını çağır
        self.student_id = student_id
    
    # Metot ezme (override)
    def introduce(self):
        print(f"Hi, I'm {self.name}, student ID: {self.student_id}")

student = Student("Mehmet", 20, "12345")
student.introduce()  # Hi, I'm Mehmet, student ID: 12345

# 3. SİHİRLİ METOTLAR (Magic Methods / Dunder Methods)
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    # String temsili
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
    
    # Uzunluk
    def __len__(self):
        return self.pages
    
    # Toplama
    def __add__(self, other):
        return Book(f"{self.title} + {other.title}", 
                   self.pages + other.pages)

book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

print(book1)           # Python Basics (200 pages)
print(len(book1))      # 200
combined = book1 + book2
print(combined)        # Python Basics + Advanced Python (500 pages)

# 4. KAPSÜLLEME (Encapsulation - Özel nitelikler)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Özel nitelik
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # HATA! Özel nitelik

# 5. SINIF METOTLARI & STATİK METOTLAR
class MathUtils:
    PI = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2
    
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.circle_area(5))  # 78.53975
print(MathUtils.add(3, 4))        # 7

# 6. PROPERTY DEKORATÖRÜ
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 86
print(temp._celsius)    # 30.0
