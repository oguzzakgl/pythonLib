# 📘 İLERİ DÜZEY PYTHON ÖZETİ
> **Not:** Bu dosya, öğrendiğiniz kritik konuların "Hızlı Başvuru" (Cheat Sheet) kaynağıdır.

---

## 1. List Comprehensions (Tek Satır Listeler)
**Ne İşe Yarar?** Döngü kurmadan tek satırda liste oluşturmanı sağlar.
**Kod:**
```python
# Klasik:
liste = []
for x in range(5): liste.append(x*2)

# Modern:
liste = [x*2 for x in range(5)]
```
**Neden?** Daha kısa, daha hızlı ve daha okunaklı.

---

## 2. Generators & Yield (Bellek Dostu Üretim)
**Ne İşe Yarar?** Verileri hafızaya (RAM) yığmadan, istendikçe tek tek üretir.
**Kod:**
```python
# Fonksiyon ile:
def sayac():
    yield 1
    yield 2

# Tek satır (Generator Expression):
gen = (x*2 for x in range(1000000)) # Köşeli değil, normal parantez!
```
**Neden?** Milyonlarca veriyi işlerken bilgisayarın donmasını engeller.

---

## 3. Decorators (Süsleyiciler - @)
**Ne İşe Yarar?** Bir fonksiyonun kodunu değiştirmeden ona yeni özellik (loglama, zaman ölçme, yetki kontrolü) ekler.
**Kod:**
```python
@zaman_olcer
def islem_yap():
    # ... kodlar ...
```
**Neden?** Kod tekrarını önler. Her fonksiyona tek tek "giriş kontrolü" yazmak zorunda kalmazsın.

---

## 4. Type Hinting (Tip İpuçları)
**Ne İşe Yarar?** Değişkenlerin ve fonksiyonların hangi tür veri (int, str) beklediğini belirtir.
**Kod:**
```python
def topla(a: int, b: int) -> int:
    return a + b
```
**Neden?** Hataları kodu çalıştırmadan (yazarken) fark edersin. VS Code sana daha iyi yardım eder.

---

## 5. Async / Await (Eş Zamansızlık)
**Ne İşe Yarar?** Bir işlemin bitmesini beklemeden diğerine geçebilmeyi sağlar (Aynı anda çok iş).
**Kod:**
```python
async def veri_getir():
    await asyncio.sleep(2) # Beklerken diğer işe geçer

# Çalıştırma:
asyncio.run(ana_program())
```
**Neden?** Web siteleri ve API işlemlerinde hızı 10 katına çıkarabilir.

---

## 6. Context Managers (with)
**Ne İşe Yarar?** Dosya veya veritabanı gibi kaynakları iş bitince otomatik kapatır.
**Kod:**
```python
# Dosya otomatik kapanır, close() gerekmez.
with open("log.txt", "w") as f:
    f.write("Merhaba")
```
**Neden?** "Dosyayı kapatmayı unuttum" hatasını ve veri kaybını önler.

---

## 7. Magic Methods (Sihirli Metotlar)
**Ne İşe Yarar?** Kendi sınıflarına (Class) Python'un yerleşik özellikleri (+, -, len, print) gibi davranma yeteneği verir.
**Kod:**
```python
class Takim:
    def __add__(self, diger): # + işareti
        # ... birleştirme kodu ...
    
    def __str__(self): # print() çıktısı
        return "Takım Adı"
```
**Neden?** Kendi yazdığın objelerle `takim1 + takim2` gibi havalı ve doğal kodlar yazabilirsin.
