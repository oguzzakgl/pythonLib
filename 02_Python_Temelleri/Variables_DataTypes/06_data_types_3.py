# Python Programlamada Koleksiyon Veri Türleri
# --------------------------------------------

# Liste (list) – değiştirilebilir, sıralıdır
liste = [10, 20, 30, "Python"]
liste.append(40)
liste[0] = 5
print("Liste:", liste)

# Demet (tuple) – değiştirilemez, sıralıdır
demet = (1, 2, 3, "Veri")
print("Tuple:", demet)
# demet[0] = 10  # TypeError: tuple değiştirilemez

# Aralık (range) – sayı aralıkları üretir
aralik = range(5)  # 0,1,2,3,4
print("Range:", list(aralik))

# Küme (set) – sırasız, benzersiz elemanlardan oluşur
kume = {1, 2, 3, 3, 2, 1}
print("Set:", kume)  # tekrar edenler tekleşir
kume.add(4)
kume.remove(2)
print("Set güncel:", kume)

# Değişmez küme (frozenset) – set'in sabit versiyonu
fs = frozenset([1, 2, 3])
print("Frozenset:", fs)
# fs.add(4)  # hata verir çünkü değiştirilemez

# Sözlük (dict) – anahtar:değer çiftlerinden oluşur
sozluk = {
    "ad": "Kaan",
    "yas": 21,
    "dil": "Python"
}
print("Sözlük:", sozluk)
print("Ad:", sozluk["ad"])
sozluk["yas"] = 22  # güncelleme
sozluk["sehir"] = "İstanbul"  # yeni ekleme
print("Güncel Sözlük:", sozluk)
del sozluk["dil"]  # silme
print("Son Sözlük:", sozluk)


# --------------------------------------------
# - list: sıralı, değiştirilebilir, [ ] ile tanımlanır.
# - tuple: sıralı ama değiştirilemez, ( ) ile tanımlanır.
# - range: aralık üretir, genelde döngülerde kullanılır.
# - set: sırasız ve benzersiz elemanlardan oluşur, küme işlemleri yapılabilir.
# - frozenset: set'in değiştirilemeyen halidir.
# - dict: key:value yapısıdır, JSON formatına benzer.
# - list ve dict en çok kullanılan veri yapılarıdır.
# - type() ile hepsinin sınıfını kontrol edebilirsin.
# - Koleksiyonlar üzerinde döngülerle gezinme, eleman ekleme, silme, güncelleme yapılabilir.
# Not: tuple ve frozenset değiştirilemez, diğerleri değiştirilebilir.
# --------------------------------------------

# ÖZET: Python'daki koleksiyon türlerini (list, tuple, set, dict, range) ve bunların temel özelliklerini, farklarını öğreniyoruz.
