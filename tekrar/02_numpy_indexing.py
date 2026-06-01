import numpy as np

veri = np.genfromtxt("tekrar/satis_verisi.csv", delimiter=",", skip_header=1,
                     usecols=(3, 4, 6, 8),
                     filling_values=np.nan)

print("Shape:", veri.shape)
# - shape: array'in boyutunu (satır, sütun) verir
# - veri.shape[0] = satır sayısı, veri.shape[1] = sütun sayısı

print("İlk 5 satır:\n", veri[:5])
# - :5 = baştan 5. indise kadar (0,1,2,3,4)
# - :5, : = tüm sütunları al

# ===== BASIC INDEXING =====
print("\n--- Basic ---")

print("İlk satır:", veri[0])
# - 0 = ilk satır, indeks 0'dan başlar
# - tek boyutlu döner

print("Son 3 satır:\n", veri[-3:])
# - -3: = sondan 3. elemandan sona kadar
# - negatif indeks sondan sayar

print("İlk 10 satır, ilk 2 sütun:\n", veri[:10, :2])
# - virgülden önce satır, sonra sütun
# - :10 = 0-9 arası satırlar
# - :2 = 0 ve 1. sütunlar

# ===== FANCY INDEXING =====
print("\n--- Fancy ---")

satirlar = [0, 10, 100, 500, 1000]
print("Seçili satırlar:\n", veri[satirlar])
# - liste vererek istediğin satırları seçersin
# - sıralı olmak zorunda değil

# ===== BOOLEAN INDEXING =====
print("\n--- Boolean ---")

yuksek = veri[veri[:, 0] > 10]
print("Adet > 10:", yuksek.shape[0], "satır")
# - veri[:, 0] = tüm satırlar, 0. sütun (adet)
# - > 10 = True/False dizisi döner
# - True olan satırlar seçilir

pahali = veri[veri[:, 1] > 200]
print("Fiyat > 200:", pahali.shape[0], "satır")
# - aynı mantık, 1. sütun (birim_fiyat)

kriter = (veri[:, 0] > 10) & (veri[:, 1] > 200)
ozel = veri[kriter]
print("Adet>10 VE Fiyat>200:", ozel.shape[0], "satır")
# - & = ve (her iki koşul da True)
# - | = veya
# - ~ = değil (tersi)

nanli = veri[np.isnan(veri).any(axis=1)]
print("En az 1 NaN içeren:", nanli.shape[0], "satır")
# - np.isnan = NaN olan hücreleri True yapar
# - .any(axis=1) = satırda en az 1 True varsa True döner
# - axis=0 = sütun bazlı, axis=1 = satır bazlı

# ===== KOŞULLU DEĞER DEĞİŞTİRME =====
print("\n--- Koşullu Değiştirme ---")

veri_kopya = veri.copy()
# - .copy() = bağımsız kopya oluşturur
# - kopyasız yaparsan orijinal değişir

veri_kopya[veri_kopya[:, 0] < 0, 0] = 1
print("Negatif adet (önce):", (veri[:, 0] < 0).sum())
print("Negatif adet (sonra):", (veri_kopya[:, 0] < 0).sum())
# - koşula uyan hücreleri seçip yeni değer atadık
# - .sum() = True'ları sayar (True=1, False=0)

sifir_fiyat = veri_kopya[:, 1] == 0
medyan = np.nanmedian(veri_kopya[:, 1])
veri_kopya[sifir_fiyat, 1] = medyan
print("Sıfır fiyat (önce):", (veri[:, 1] == 0).sum())
print("Sıfır fiyat (sonra):", (veri_kopya[:, 1] == 0).sum())
# - np.nanmedian = NaN'ları yok sayarak medyan hesaplar
# - sıfır olan fiyatları medyanla değiştirdik

print("\n✅ Indexing tamam.")