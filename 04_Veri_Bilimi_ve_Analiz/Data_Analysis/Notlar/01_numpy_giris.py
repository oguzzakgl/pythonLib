# 01_numpy_giris.py
# Bu ders, Python listeleri ile NumPy dizileri (arrays) arasındaki farkı
# ve NumPy'ın temel özelliklerini anlatır.

import numpy as np
import time

print("--- 1. LİSTE vs NUMPY ARRAY ---")

# Python Listesi
python_listesi = [1, 2, 3, 4, 5]
print(f"Python Listesi: {python_listesi}")

# NumPy Dizisi (Array)
# Avantajı: Çok daha hızlıdır ve vektörel işlem (tek seferde tüm elemanlara işlem) yapabilir.
numpy_dizisi = np.array([1, 2, 3, 4, 5])
print(f"NumPy Dizisi:   {numpy_dizisi}")

print("\n--- 2. VEKTÖREL İŞLEMLER (BÜYÜLÜ KISIM) ---")
# Listelerde her elemanı 2 ile çarpmak için döngü gerekir:
yeni_liste = []
for x in python_listesi:
    yeni_liste.append(x * 2)
print(f"Liste Çarpımı (Döngü ile): {yeni_liste}")

# NumPy'da ise direkt çarpabiliriz (Döngü yok!):
# Bu işlem C dilinde optimize edilmiştir, binlerce kat hızlı olabilir.
yeni_dizi = numpy_dizisi * 2
print(f"NumPy Çarpımı (Direkt):    {yeni_dizi}")

print("\n--- 3. HIZ TESTİ (NEDEN NUMPY?) ---")
boyut = 1_000_000  # 1 Milyon eleman
buyuk_liste = list(range(boyut))
buyuk_dizi = np.arange(boyut)

# Liste Testi
basla = time.time()
liste_sonuc = [x * 2 for x in buyuk_liste]
bitis = time.time()
print(f"Python Listesi Süresi: {bitis - basla:.5f} saniye")

# NumPy Testi
basla = time.time()
dizi_sonuc = buyuk_dizi * 2
bitis = time.time()
print(f"NumPy Dizisi Süresi:   {bitis - basla:.5f} saniye")


print("\n--- 4. İSTATİSTİKSEL İŞLEMLER ---")
notlar = np.array([45, 60, 75, 80, 90, 100, 30])
print(f"Notlar: {notlar}")
print(f"Ortalama: {notlar.mean():.2f}")
print(f"En Yüksek: {notlar.max()}")
print(f"En Düşük:  {notlar.min()}")

# Filtreleme (Maskeleme)
gecenler = notlar[notlar >= 50]
print(f"Gecen Notlar (>=50): {gecenler}")
