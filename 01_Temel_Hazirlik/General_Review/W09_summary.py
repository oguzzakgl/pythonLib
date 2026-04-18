# W09: Dosya İşlemleri - Özet
# ============================

# 1. DOSYA OKUMA
# Mod 'r' (read - varsayılan)
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()  # Tüm dosyayı oku
    print(content)

# Satır satır oku
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # Yeni satır karakterini kaldır

# Belirli sayıda karakter oku
with open("example.txt", "r", encoding="utf-8") as file:
    chunk = file.read(10)  # İlk 10 karakteri oku
    print(chunk)

# 2. DOSYAYA YAZMA
# Mod 'w' (write - mevcut dosyanın üzerine yazar)
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# Birden fazla satır yaz
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

# 3. DOSYAYA EKLEME
# Mod 'a' (append - dosyanın sonuna ekler)
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("New log entry\n")

# 4. DOSYA MODLARI
# 'r'  - Okuma (varsayılan)
# 'w'  - Yazma (üzerine yazar)
# 'a'  - Ekleme (sona ekler)
# 'r+' - Okuma ve yazma
# 'b'  - İkili mod (örn: 'rb', 'wb')

# 5. CONTEXT MANAGER (with ifadesi)
# Dosyayı otomatik kapatır, hata olsa bile
with open("file.txt", "r") as file:
    data = file.read()
# Dosya burada otomatik olarak kapatılır

# Context manager olmadan (önerilmez):
# file = open("file.txt", "r")
# data = file.read()
# file.close()  # Kapatmayı unutmamak gerekir!

# 6. HATA YÖNETİMİ
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Dosya bulunamadı!")
except PermissionError:
    print("Dosyaya erişim izni yok!")

# 7. DOSYA VARLIĞINI KONTROL ETME
import os

if os.path.exists("file.txt"):
    print("Dosya mevcut")
else:
    print("Dosya mevcut değil")

# 8. DOSYA İŞLEMLERİ
# Dosya boyutunu al
size = os.path.getsize("file.txt")
print(f"Dosya boyutu: {size} byte")

# Dosyayı sil
# os.remove("file.txt")

# Dosyayı yeniden adlandır
# os.rename("old.txt", "new.txt")

# 9. YOLLARLA ÇALIŞMA
from pathlib import Path

# Path nesnesi oluştur
path = Path("folder/subfolder/file.txt")
print(path.name)       # file.txt
print(path.parent)     # folder/subfolder
print(path.suffix)     # .txt

# Yolun var olup olmadığını kontrol et
if path.exists():
    print("Yol mevcut")

# 10. PRATIK ÖRNEK: LOG DOSYASI
def log_message(message):
    with open("app.log", "a", encoding="utf-8") as file:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

# log_message("Uygulama başlatıldı")
# log_message("Kullanıcı giriş yaptı")
