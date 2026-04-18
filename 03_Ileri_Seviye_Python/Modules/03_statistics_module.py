# Konu: Statistics ModÃ¼lÃ¼
# AmaÃ§: Ä°statistiksel hesaplamalar (ortalama, medyan, mod, standart sapma vb.).

import statistics

data = [10, 20, 30, 40, 50]
data1 = ["apple", "banana", "cherry", "date", "apple", "banana", "apple"]

print(statistics.mean(data))        # Aritmetik ortalama,
print(statistics.harmonic_mean(data))  # Harmonik ortalama
print(statistics.geometric_mean(data)) # Geometrik ortalama
print(statistics.median(data))      # Medyan
print(statistics.mode(data))        # Mod
print(statistics.mode(data1))        # Mod
print(statistics.multimode(data1))  # Ã‡oklu mod
print(statistics.stdev(data))      # Standart sapma
print(statistics.variance(data))    # Varyans
print(statistics.pvariance(data))   # PopÃ¼lasyon varyansÄ±
print(statistics.quantiles(data, n=4))  # Ã‡eyreklik deÄŸerler
print(statistics.median_low(data))  # DÃ¼ÅŸÃ¼k medyan
print(statistics.median_high(data)) # YÃ¼ksek medyan
print(statistics.fmean(data))       # Float ortalama
# ÖZET: Veri grupları üzerinde ortalama (mean), medyan, mod ve standart sapma gibi temel istatistiksel hesaplamaları hızlıca yapmamızı sağlayan 'statistics' modülünü tanıyoruz.
