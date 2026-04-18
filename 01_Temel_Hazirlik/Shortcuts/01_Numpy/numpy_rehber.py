# 🔢 Numpy Rehberi (Gerçek Veri Seti İle)
# Ortak Veri Seti: ../ortak_veri.csv

import numpy as np
import os

# Dosya yolunu belirleyelim (Bu script'in olduğu klasörün bir üstüne çıkıp dosyayı bulur)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'ortak_veri.csv')

print(f"--- VERİ OKUNUYOR: {csv_path} ---")

# ==========================================
# 1. CSV'den Veri Okuma (Sadece Sayısal Sütunlar)
# ==========================================
# Numpy genfromtxt, CSV okumak için kullanılır.
# usecols=(4, 5): Sadece Fiyat (4. indeks) ve Adet (5. indeks) sütunlarını al.
# skip_header=1: Başlık satırını atla.
data = np.genfromtxt(csv_path, delimiter=',', skip_header=1, usecols=(4, 5))

print("\n--- Ham Veri (İlk 5 Satır) ---")
print(data[:5]) 

# Sütunları Ayıralım
fiyatlar = data[:, 0] # 0. sütun aslında Fiyat
adetler = data[:, 1]  # 1. sütun aslında Adet


# ==========================================
# 2. Matematiksel İşlemler
# ==========================================
print("\n--- Hesaplamalar ---")

# Toplam Satış Tutarı (Fiyat * Adet) - Vektörel Çarpım
satis_tutarlari = fiyatlar * adetler
print(f"Her satışın tutarı (İlk 3): {satis_tutarlari[:3]}")

# Toplam Ciro
toplam_ciro = satis_tutarlari.sum()
print(f"Toplam Ciro: {toplam_ciro} TL")

# Ortalama Fiyat
print(f"Ortalama Ürün Fiyatı: {fiyatlar.mean()} TL")


# ==========================================
# 3. Filtreleme (Koşullu Analiz)
# ==========================================
print("\n--- Filtreleme ---")

# Fiyatı 5000 TL'den pahalı olan satışlar
pahali_urunler = fiyatlar[fiyatlar > 5000]
print(f"5000 TL üzeri fiyatlar: {pahali_urunler}")
print(f"Kaç adet pahalı satış var?: {len(pahali_urunler)}")

# np.where ile koşul
# Ciro 50.000'den büyükse 'Yüksek', değilse 'Düşük'
performans = np.where(satis_tutarlari > 50000, 'Yüksek Ciro', 'Düşük Ciro')
print(f"\nSatış Performansları (İlk 5):\n{performans[:5]}")
