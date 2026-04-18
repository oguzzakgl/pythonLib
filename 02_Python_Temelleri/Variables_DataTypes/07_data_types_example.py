# 1) input -> int -> erişkin kontrolü
yas_metin = "19"                 # input() yerine sabit; deneme: "19"
yas = int(yas_metin)             # "19" -> 19
print("erişkin" if yas >= 18 else "reşit değil")

# 2) "12.300" -> float -> gerekirse int
s = "12.300"
v = float(s)                      # 12.3
print(int(v) if v.is_integer() else v)

# 3) "1,234" -> "1.234" -> float
duzeltilmis = "1,234".replace(",", ".")
print(float(duzeltilmis))         # 1.234

# 4) "True"/"False" -> bool (fonksiyonsuz)
b_metin = "True"                  # deneme: "true", "FALSE", "evet", "1"
norm = b_metin.strip().lower()
b_deger = norm in {"true", "1", "yes", "y", "evet"}
print(b_deger)

# 5) "5.7" -> float -> int
print(int(float("5.7")))          # 5

# 6) Güvenli int dönüşümü (fonksiyonsuz try/except)
metin = "abc"
try:
    sayi = int(metin)
except ValueError:
    sayi = None
print(sayi)                       # None

# 7) Tekrarsız SIRALI liste
lst = [1, 2, 2, 3, 3, 3]
benzersiz = sorted(set(lst))      # {1,2,3} -> [1,2,3]
print(benzersiz)

# 8) 1..100 arası çiftler (döngüsüz)
ciftler = list(range(2, 101, 2))
print(ciftler[:10], "...", len(ciftler), "adet")  # ilk 10 ve adet

# 9) tuple <-> list
t = (1, 2, 3)
l = list(t)                       # (1,2,3) -> [1,2,3]
t2 = tuple(l)                     # [1,2,3] -> (1,2,3)
print(l, t2)

# 10) frozenset ve değişmezlik
fs = frozenset({1, 2, 2, 3})
print(fs)
# fs.add(4)  # AttributeError: frozenset değiştirilemez

# 11) dict alanını dönüştür
d = {"ad": "Kaan", "yas": "21"}
d["yas"] = int(d["yas"])          # "21" -> 21
print(d)

# 12) Karışık diziden sayıya çevrilebilenleri seç (fonksiyonsuz, kısa örnek)
raw = ["10", "3.5", "x", True, "-2"]
nums = []

# Eleman 0
try: nums.append(float(raw[0]))
except (ValueError, TypeError): pass
# Eleman 1
try: nums.append(float(raw[1]))
except (ValueError, TypeError): pass
# Eleman 2
try: nums.append(float(raw[2]))
except (ValueError, TypeError): pass
# Eleman 3
try: nums.append(float(raw[3]))
except (ValueError, TypeError): pass
# Eleman 4
try: nums.append(float(raw[4]))
except (ValueError, TypeError): pass

print(nums)

# ---------------------------------
# 🧠 NOTLAR
# - type() türü verir; bool("") -> False, bool("0") -> True (boş olmayan her str True).
# - range hafızada liste tutmaz; list(range(...)) ile maddileştirilir.
# - set benzersizleştirir; frozenset değiştirilemez.
# - int("5.0") ValueError verir; önce float("5.0"), sonra int() uygulayın.
# - try/except, hatalı metinleri güvenle yönetir; üretimde zorunludur.
# ---------------------------------

# ÖZET: Veri türleri ve dönüşümleriyle ilgili veri temizleme, güvenli dönüştürme ve koleksiyon manevraları gibi pratik senaryoları uyguluyoruz.
