# Konu: Tip Dönüşümü Örneği
# Amaç: Kullanıcıdan alınan string veriyi float'a çevirerek daire hesaplamaları yapma.

# dairenin yarıçapını kullanıcıdan alıpa alan ve çevresini hesaplayan program

# dairenin alanı = pi * r^2
# dairenin çevresi = 2 * pi * r

pi = 3.14159
yaricap = float(input("Dairenin yarıçapını girin: "))
cevre = 2 * pi * yaricap
alan = pi * yaricap ** 2
print("Dairenin çevresi:", cevre)
print("Dairenin alanı:", alan)
# ---------------------------------

# ÖZET: Kullanıcıdan alınan metin verilerini sayısal tiplere dönüştürerek matematiksel hesaplamalar yapmayı öğreniyoruz.
