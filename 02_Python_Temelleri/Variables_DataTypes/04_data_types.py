print(type(tam_sayi))
print(type(ondalik_sayi))
print(type(karmaşık_sayi))

# Metin türü (string)
isim = "Kaan"
print(type(isim))
print("Ad:", isim)

# Mantıksal tür (bool)
aktif_mi = True
print(type(aktif_mi))
print("Aktif kullanıcı mı:", aktif_mi)

# Dönüştürme örnekleri
sayi_str = str(tam_sayi)
print(sayi_str, type(sayi_str))

sayi_float = float(tam_sayi)
print(sayi_float, type(sayi_float))

# Tip dönüşümü hatası örneği
try:
    print(int("abc"))
except ValueError:
    print("Bu ifade sayıya dönüştürülemez.")

# 6️⃣ type() ve isinstance() farkı
print(type(10) == int)             # True
print(isinstance(10, (int, float))) # True

# ---------------------------------

# ÖZET: Temel veri türlerini (int, float, str, bool, complex) ve bunlar arasındaki güvenli dönüşüm yöntemlerini öğreniyoruz.
# - Temel veri türleri: int, float, str, bool, complex.
# - type() ve isinstance() tür kontrolü için kullanılır.
# - Tür dönüşümleri: int(), float(), str(), bool().
# - Hatalı dönüşümler ValueError ile sonuçlanır.
# - isinstance() birden fazla tür kontrolüne izin verir.
# ---------------------------------