# Konu: Listelerle Döngü Kullanımı
# Amaç: for, while döngüleri ve List Comprehension ile liste üzerinde gezinme yöntemleri.

# Ana veri listesi
fruits = ["apple", "banana", "cherry", "orange"]

# --- Yöntem 1: 'for' döngüsü (indeks ile) ---
# Yorum satırı kaldırıldı ve düzeltildi.
print("--- Yöntem 1: 'for' ve 'range(len())' ---")
for item_index in range(len(fruits)):
    # len(fruits) -> 4
    # range(4) -> 0, 1, 2, 3
    # fruits[0], fruits[1], ...
    print(fruits[item_index])


# --- Yöntem 2: 'while' döngüsü ---
# Yorum satırı kaldırıldı.
print("\n--- Yöntem 2: 'while' döngüsü ---")
i = 0  # Başlangıç indeksi
while i < len(fruits): # Koşul: İndeks, liste uzunluğundan küçük olduğu sürece
    print(fruits[i])
    i += 1 # İndeksi artır (sonsuz döngüyü önler)


# --- Yöntem 3: List Comprehension (Liste Anlama) ---

# 3a: Yazdırma işlemi (Genellikle tercih edilmez, asıl amaç liste oluşturmaktır)
print("\n--- Yöntem 3a: List Comprehension (Yazdırma) ---")
[print(item) for item in fruits]
# Bu, aşağıdaki kodun tek satırlık halidir:
# for item in fruits:
#     print(item)


# 3b: Filtreleyerek yeni liste oluşturma
print("\n--- Yöntem 3b: List Comprehension (Filtreleme) ---")
new_list = [item for item in fruits if ("a" in item)]
# 'fruits' listesindeki "a" harfi içeren 'item' öğelerini seçerek 'new_list' oluşturur.
print(f"İçinde 'a' olanlar: {new_list}")


# 3c: 'range' kullanarak yeni liste oluşturma (Kodunuzdaki son satır)
print("\n--- Yöntem 3c: List Comprehension ('range' ile) ---")
# range(10) -> 0'dan 9'a kadar olan sayıları üretir
sayilar = [item for item in range(10)]
# Bu sayıları bir listeye [0, 1, 2, ..., 9] olarak atar.
print(f"0'dan 9'a sayılar: {sayilar}")
# �ZET: Listelerin i�indeki verileri d�ng�ler (for, while) ve tek sat�rl�k pratik bir y�ntem olan 'List Comprehension' ile i�lemeyi ��reniyoruz.
