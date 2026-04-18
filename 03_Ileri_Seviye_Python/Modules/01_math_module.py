# Konu: Math Modülü
# Amaç: Matematiksel fonksiyonlar (karekök, faktöriyel, trigonometri vb.) kullanımı.

import math

min_value=min(10, 20, 5, -3, 15)    #en küçük değeri bulur
max_value=max(10, 20, 5, -3, 15)    #en büyük değeri bulur

print(min_value)
print(max_value)

mutlak_sayi = abs(-7)    #mutlaka pozitif yapar
print(mutlak_sayi)

us_alma = pow(2, 3)    #üs alma işlemi yapar
print(us_alma)

print(math.e)    #e sayısı
print(math.pi)   #pi sayısı
print(math.inf)  #sonsuzluk değeri
print(-math.inf)    #negatif sonsuzluk değeri
print(math.nan)   #not a number değeri
print(math.tau)  #tau sayısı


print(math.acos(1))   #arka kosinüs değeri
print(math.asin(0))   #arka sinüs değeri
print(math.atan(1))   #arka tanjant değeri
print(math.cos(math.pi/2))   #kosinüs değeri
print(math.sin(math.pi/2))   #sinüs değeri
print(math.tan(math.pi/4))   #tanjant değeri
print(math.degrees(math.pi))   #radyan değeri dereceye çevirir
print(math.radians(180))   #dereceyi radyan değere çevir
print(math.hypot(3, 4))   #hipotenüs değeri
print(math.log(math.e))   #e tabanında logaritma değeri
print(math.log10(100))   #10 tabanında logaritma değeri
print(math.sqrt(16))   #karekök değeri
print(math.isqrt(25))   #tam karekök değeri
print(math.factorial(5))   #faktöriyel değeri
print(math.ceil(4.2))   #yukarı yuvarlama işlemi
print(math.floor(4.7))   #aşağı yuvarlama işlemi
print(math.fabs(-5.5))   #mutlak değer
print(math.fmod(20, 3))   #mod alma işlemi
print(math.gcd(48, 18))   #en büyük ortak bölen
print(math.lcm(4, 6))   #en küçük ortak kat
print(math.isfinite(10))   #sonlu mu kontrolü
print(math.isinf(math.inf))   #sonsuz mu kontrolü
print(math.isnan(math.nan))   #not a number mı kontrolü
print(math.trunc(4.9))   #ondalık kısmı atma işlemi
print(math.copysign(3, -2))   #işaret kopyalama işlemi


print(math.comb(5, 2))   #kombinasyon değeri
print(math.perm(5, 2))   #permutasyon değeri
print(math.prod([1, 2, 3, 4]))   #çarpım değeri
print(math.dist([1, 2], [4, 6]))   #iki nokta arasındaki uzaklık
print(math.erf(1))   #hata fonksiyonu değeri
print(math.erfc(1))   #tamamlayıcı hata fonksiyonu değeri
print(math.gamma(5))   #gamma fonksiyonu değeri
print(math.lgamma(5))   #log gamma fonksiyonu değeri
print(math.modf(4.7))   #ondalık ve tam kısmı ayırma işlemi

# �ZET: Python'un haz�r 'math' k�t�phanesini kullanarak; karek�k, fakt�riyel, logaritma ve trigonometri gibi karma��k matematiksel i�lemleri tek sat�rda yapmay� ��reniyoruz.
