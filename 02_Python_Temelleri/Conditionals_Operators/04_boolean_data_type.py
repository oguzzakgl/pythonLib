# --- 1. bool Değerlerini Doğrudan Tanımlama ---

# 'bool' veri türü, bir durumun DOĞRU (True) veya YANLIŞ (False) olduğunu belirtir.
# Bu değerler, programlamada "karar verme" mekanizmasının temelidir.
# Not: Python'da 'T' ve 'F' harfleri büyük yazılmalıdır.

program_calisiyor_mu = True
kapi_acik_mi = False

print(f"Program çalışıyor mu? : {program_calisiyor_mu}")
print(f"Kapı açık mı? : {kapi_acik_mi}")
print(f"Bu değerin türü: {type(program_calisiyor_mu)}") # Çıktı: <class 'bool'>

print("-" * 30) # Ayraç

# --- 2. Karşılaştırma Operatörleri ile bool Değerleri Üretme ---
# 'bool' değerleri çoğunlukla iki değeri karşılaştırdığımızda sonuç olarak ortaya çıkar.
# Bu operatörler her zaman 'True' veya 'False' döndürür.

# ==  (Eşit mi?)
# !=  (Eşit değil mi?)
# >   (Büyük mü?)
# <   (Küçük mü?)
# >=  (Büyük veya eşit mi?)
# <=  (Küçük veya eşit mi?)

yas = 20
ehliyet_yasi = 18

# 'yas >= ehliyet_yasi' işlemi bir karşılaştırmadır ve sonucu 'bool'dur.
ehliyet_alabilir_mi = (yas >= ehliyet_yasi) # (20 >= 18) işlemi 'True' sonucunu verir

print(f"Kişinin yaşı: {yas}")
print(f"Ehliyet yaşı: {ehliyet_yasi}")
print(f"Kişi ehliyet alabilir mi? : {ehliyet_alabilir_mi}") # Çıktı: True

print("-" * 30) # Ayraç

# Diğer karşılaştırma örnekleri:
sayi1 = 10
sayi2 = 5

print(f"Sayi1 ({sayi1}), Sayi2'ye ({sayi2}) eşit mi? : {sayi1 == sayi2}") # Çıktı: False
print(f"Sayi1 ({sayi1}), Sayi2'den ({sayi2}) farklı mı? : {sayi1 != sayi2}") # Çıktı: True
print(f"Sayi1 ({sayi1}), Sayi2'den ({sayi2}) küçük mü? : {sayi1 < sayi2}") # Çıktı: False

print("-" * 30) # Ayraç

# --- 3. 'bool()' Fonksiyonu - "Truthiness" (Doğruluk) ve "Falsiness" (Yanlışlık) ---

# Python'da her veri türünün bir 'bool' karşılığı vardır.
# Bazı değerler "Yanlış" (False) kabul edilir, geri kalan her şey "Doğru" (True) kabul edilir.
# 'bool(deger)' fonksiyonu ile bir değerin bool karşılığını görebiliriz.

# --- "Falsy" (Yanlış kabul edilen) Değerler ---
# Bu değerler 'if' kontrolüne girdiklerinde 'False' olarak davranırlar.

# 1. Sayısal sıfırlar
print(f"bool(0)    değeri: {bool(0)}")     # Tamsayı 0
print(f"bool(0.0)  değeri: {bool(0.0)}")   # Ondalıklı 0
# 2. Boş koleksiyonlar (veri yapıları)
print(f"bool('')   değeri: {bool('')}")     # Boş string (metin)
print(f"bool([])   değeri: {bool([])}")     # Boş liste
print(f"bool(())   değeri: {bool(())}")     # Boş demet (tuple)
# 3. Özel 'None' değeri (Hiçlik/Boşluk belirtir)
print(f"bool(None) değeri: {bool(None)}")

print("-" * 30) # Ayraç

# --- "True" (Doğru kabul edilen) Değerler ---
# Yukarıdakiler dışında kalan HER ŞEY 'True' kabul edilir.

print(f"bool(10)   değeri: {bool(10)}")   # Sıfır olmayan sayı
print(f"bool(-5)   değeri: {bool(-5)}")   # Negatif sayı
print(f"bool('a')  değeri: {bool('a')}")  # Dolu string
print(f"bool('False') değeri: {bool('False')}") # 'False' yazan bir string bile 'True'dur!
print(f"bool([1, 2]) değeri: {bool([1, 2])}") # Dolu liste

print("-" * 30) # Ayraç

# --- 4. Koşullu İfadelerde (if) 'bool' Kullanımı ---

# 'if' bloğu, çalışmak için kendisinden sonra gelen ifadenin 'True' olmasını bekler.

# 4a. Doğrudan 'True'/'False' kullanmak (nadiren yapılır)
if True:
    print("'if True' bloğu her zaman çalışır.")

if False:
    print("'if False' bloğu asla çalışmaz.") # Bu satır EKRANA ÇIKMAZ

# 4b. Karşılaştırma sonucu kullanmak (En yaygın kullanım)
kullanici_yasi = 17
if kullanici_yasi >= 18:
    # (17 >= 18) işlemi 'False' döndürdüğü için bu blok ATLANIR.
    print("Giriş yapabilirsiniz (1).")
else:
    # Üstteki 'if' bloğu 'False' olduğu için 'else' bloğu çalışır.
    print("Giriş yapamazsınız, yaşınız küçük (1).")


# 4c. "Truthiness" kullanarak kontrol etmek
# Bu, bir değişkenin "dolu" mu "boş" mu olduğunu kontrol etmenin kısa yoludur.
kullanici_adi = input("Kullanıcı adınızı giriniz (Test için boş bırakıp Enter'a basın): ")

# Eğer kullanıcı_adi boşsa (""), bool("") 'False' olur ve 'if' çalışmaz.
# Eğer kullanıcı_adi doluysa (örn: "ahmet"), bool("ahmet") 'True' olur ve 'if' çalışır.
if kullanici_adi: 
    print(f"Hoş geldin, {kullanici_adi}")
else:
    # 'kullanici_adi' boş ("") ise, yani 'Falsy' ise burası çalışır
    print("Kullanıcı adı girmediniz!")

print("-" * 30) # Ayraç

# --- 5. Mantıksal Operatörler ('and', 'or', 'not') ile 'bool' Birleştirme ---

# 'bool' değerleri birleştirerek daha karmaşık kararlar alabiliriz.

# 'and' (ve): Her iki taraf da 'True' ise sonuç 'True' olur.
# 'or'  (veya): Taraflardan en az biri 'True' ise sonuç 'True' olur.
# 'not' (değil): 'True' ise 'False' yapar, 'False' ise 'True' yapar.

yas = 22
mezun_mu = True
saglik_sorunu_var_mi = False

# Örnek 1: Askerlik durumu (20 yaşından büyük VE mezun OLMALI)
# (yas > 20) -> (22 > 20) -> True
# (mezun_mu) -> True
# (True and True) -> Sonuç: True
if yas > 20 and mezun_mu:
    print("Askerlik için uygunsunuz.")
else:
    print("Askerlik için uygun değilsiniz.")

# Örnek 2: İndirimli bilet (25 yaşından küçük VEYA mezun DEĞİLSE (öğrenciyse))
# (yas < 25) -> (22 < 25) -> True
# (not mezun_mu) -> (not True) -> False
# (True or False) -> Sonuç: True
if yas < 25 or not mezun_mu:
    print("İndirimli bilet alabilirsiniz.")
else:
    print("Tam bilet almalısınız.")

# Örnek 3: Ehliyet (18 yaşından büyük VE sağlık sorunu YOKSA)
# (yas > 18) -> (22 > 18) -> True
# (not saglik_sorunu_var_mi) -> (not False) -> True
# (True and True) -> Sonuç: True
if yas > 18 and not saglik_sorunu_var_mi:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")