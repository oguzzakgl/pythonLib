# W02: String'ler - Özet
# =======================

# 1. STRING TEMELLERİ
text = "Python Programming"
print(len(text))  # Uzunluk
print(text.upper())  # PYTHON PROGRAMMING
print(text.lower())  # python programming

# 2. STRING DİLİMLEME
# [başlangıç:bitiş:adım]
print(text[0:6])  # Python
print(text[::-1])  # Ters çevir: gnimmargorP nohtyP
print(text[::2])  # Her 2. karakter

# 3. STRING METOTLARI
message = "  hello world  "
print(message.strip())  # Boşlukları kaldır
print(message.replace("world", "Python"))  # Değiştir
print(message.split())  # Listeye böl

# 4. KAÇIŞ DİZİLERİ
escaped = "Line 1\nLine 2\tTabbed"
print(escaped)

# 5. STRING FORMATLAMA
name = "Ali"
age = 25

# Eski stil
print("Name: %s, Age: %d" % (name, age))

# format()
print("Name: {}, Age: {}".format(name, age))

# f-string (Modern)
print(f"Name: {name}, Age: {age}")

# 6. YAYGN İŞLEMLER
text = "Python"
print(text.startswith("Py"))  # True
print(text.endswith("on"))  # True
print("Py" in text)  # True (üyelik)
print(text.find("th"))  # 2 (indeks)
print(text.count("o"))  # 1
