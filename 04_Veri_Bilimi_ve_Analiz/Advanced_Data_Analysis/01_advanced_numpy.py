import numpy as np

# ==========================================
# İLERİ SEVİYE NUMPY (ADVANCED NUMPY)
# ==========================================
print("--- İLERİ SEVİYE NUMPY DERSLERİ ---\n")

# 1. Broadcasting (Yayınlama)
# Numpy'ın farklı şekillerdeki dizilerle aritmetik işlem yapabilme yeteneğidir.
print("1. Broadcasting Örneği:")
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]]) 
# a'nın şekli (3,), b'nin şekli (3,1)
# Sonuç (3,3) olacak.
c = a + b
print(f"a: {a}")
print(f"b: \n{b}")
print(f"a + b Sonucu: \n{c}")
print("-" * 30)

# 2. Fancy Indexing (Süslü İndeksleme)
# Belirli indeksleri bir liste veya dizi olarak vererek seçme işlemi.
print("2. Fancy Indexing:")
arr = np.random.randint(0, 100, 10)
print(f"Orijinal Dizi: {arr}")
indices = [1, 3, 5]
print(f"Seçilen İndeksler [1, 3, 5]: {arr[indices]}")

# Boolean Masking ile birlikte kullanımı
mask = arr > 50
print(f"50'den büyük elemanlar: {arr[mask]}")
print("-" * 30)

# 3. Lineer Cebir İşlemleri (Linear Algebra)
print("3. Lineer Cebir (Linear Algebra):")
# 2x2'lik iki matris
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# Matris Çarpımı (Dot Product)
dot_product = np.dot(m1, m2) # veya m1 @ m2
print(f"Matris Çarpımı (m1 @ m2): \n{dot_product}")

# Determinant
det = np.linalg.det(m1)
print(f"m1 Determinantı: {det:.2f}")

# Tersi (Inverse)
inv = np.linalg.inv(m1)
print(f"m1 Tersi: \n{inv}")
print("-" * 30)

# 4. Reshaping ve Stacking (Şekil Değiştirme ve Yığma)
print("4. Reshaping ve Stacking:")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Dikey Yığma (Vertical Stack)
v_stack = np.vstack((x, y))
print(f"Dikey Yığma (vstack): \n{v_stack}")

# Yatay Yığma (Horizontal Stack)
h_stack = np.hstack((x, y))
print(f"Yatay Yığma (hstack): {h_stack}")

# 3 Boyutlu Dizi Oluşturma
d3 = np.arange(24).reshape(2, 3, 4)
print(f"3 Boyutlu Dizi (2 blok, 3 satır, 4 sütun): \n{d3}")

# �ZET: NumPy'�n ileri seviye �zellikleri olan Broadcasting (yay�nlama), Fancy Indexing ve matris �arp�m�/deteremimant gibi lineer cebir i�lemlerini detayl�ca inceliyoruz.
