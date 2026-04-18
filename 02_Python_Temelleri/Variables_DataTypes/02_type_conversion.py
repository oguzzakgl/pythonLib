# Konu: Tür Belirleme ve Dönüştürme
# Amaç: Python'daki tüm veri tiplerini tanıma ve aralarında dönüşüm yapma.

# Sayısal ve metin türleri
i = 42                         # int
f = 3.14                       # float
c = 2 + 3j                     # complex
s = "Python"                   # str

# Koleksiyon türleri
lst = [1, 2, 3]                # list
tup = (1, 2, 3)                # tuple
st  = {1, 2, 2, 3}             # set  -> {1,2,3}
fst = frozenset([1, 2, 3])     # frozenset
rng = range(5)                 # range -> 0..4
dct = {"ad": "Kaan", "yas": 21}# dict
b   = True                     # bool

# type() çıktıları
print(type(i), type(f), type(c), type(s))
print(type(lst), type(tup), type(st), type(fst), type(rng), type(dct), type(b))

# isinstance örnekleri
print(isinstance(i, int))                 # True
print(isinstance(f, (int, float)))        # True
print(isinstance(lst, (list, tuple)))     # True
print(isinstance(fst, frozenset))         # True
print(isinstance(b, bool))                # True

# Temel dönüşümler
print(int("123"))              # str -> int
print(float("3.5"))            # str -> float
print(str(999))                # int -> str
print(list(rng))               # range -> list
print(tuple(lst))              # list -> tuple
print(set([1,1,2,3]))          # list -> set (tekrarsız)
print(frozenset(st))           # set -> frozenset

# Hatalı dönüşüm yakalama
try:
    x = int("12.3")  # ValueError
except ValueError:
    print("Hatalı dönüşüm: '12.3' doğrudan int'e çevrilemez.")

# ---------------------------------
# - type(x) nesnenin gerçek türünü verir; isinstance(x, T) tip ailesi kontrolüne uygundur.
# - bool("") -> False, bool("0") -> True; boş olmayan her str True kabul edilir.
# - range hafızada liste tutmaz; list(range(n)) ile maddileştirilebilir.
# - set benzersiz eleman tutar, frozenset değiştirilemeyen settir (hash'lenebilir).
# - tuple değiştirilemez, list değiştirilebilir; tuple performans ve güvenlik için tercih edilebilir.
# - int("5.0") hata verir; önce float("5.0") sonra int() uygulanmalıdır.
# ---------------------------------

# ÖZET: Python'daki veri tiplerini tanımayı, tip kontrolü yapmayı ve tipler arası dönüşüm (casting) işlemlerini öğreniyoruz.
