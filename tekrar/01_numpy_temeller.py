"""
NumPy Temeller (array oluşturma, shape, reshape, dtype)
"""

import numpy as np

import numpy as np

# ===== ARRAY OLUŞTURMA =====
# Listeden
a = np.array([1, 2, 3, 4, 5])

# Belli aralık
b = np.arange(0, 10, 2)      # 0,2,4,6,8
c = np.linspace(0, 100, 5)   # 0-100 arası 5 eşit parça

# Özel array'ler
d = np.zeros((3, 3))         # 3x3 sıfır
e = np.ones((2, 4))          # 2x4 bir
f = np.eye(3)                # 3x3 birim matris
g = np.full((2, 3), 7)       # 2x3 hepsi 7

# Rastgele
np.random.seed(42)
h = np.random.randint(0, 100, 10)   # 0-100 arası 10 tam sayı
i = np.random.rand(5)               # 0-1 arası 5 ondalık
j = np.random.randn(5)              # normal dağılım, ort=0, std=1

# ===== ÇOK BOYUTLU =====
matris_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matris_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# ===== ÖZELLİKLER =====
dizi = np.random.randint(10, 100, (4, 5))
dizi.ndim      # boyut sayısı
dizi.shape     # (satır, sütun)
dizi.size      # toplam eleman
dizi.dtype     # veri tipi

# ===== SHAPE DEĞİŞTİRME =====
dizi = np.arange(1, 13)
dizi.reshape(3, 4)     # 3x4 yap
dizi.reshape(2, 2, 3)  # 2x2x3 yap
matris_2d.flatten()    # 1 boyuta indir
matris_2d.ravel()      # flatten gibi ama daha hızlı
matris_2d.T            # transpose

# ===== VERİ TİPİ DÖNÜŞÜMÜ =====
dizi.astype(np.float64)  # int -> float
dizi.astype(str)         # -> string
dizi.astype(bool)        # -> True/False (0 hariç hepsi True)

# ===== MİNİ PROJE: NOT ANALİZİ =====
np.random.seed(123)
notlar = np.random.randint(30, 101, (10, 4))  # 10 öğrenci, 4 sınav

ogrenci_ort = notlar.mean(axis=1)    # her öğrencinin ortalaması
sinav_ort = notlar.mean(axis=0)      # her sınavın ortalaması

print("En yüksek ortalama:", ogrenci_ort.max(), "Öğrenci:", ogrenci_ort.argmax() + 1)
print("En düşük ortalama:", ogrenci_ort.min(), "Öğrenci:", ogrenci_ort.argmin() + 1)
print("Sınıf ortalaması:", notlar.mean().round(2))
print("60 altı not sayısı:", (notlar < 60).sum())