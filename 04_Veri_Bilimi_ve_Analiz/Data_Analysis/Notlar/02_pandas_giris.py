# 02_pandas_giris.py
# Pandas, Python'un "Excel"idir. Veri analizi için DataFrame yapısını kullanır.

import pandas as pd

print("--- 1. DATAFRAME OLUŞTURMA ---")
# Veriyi genelde bir sözlük (dictionary) olarak tanımlarız:
veri = {
    "İsim": ["Ahmet", "Mehmet", "Ayşe", "Fatma"],
    "Yaş": [25, 30, 22, 28],
    "Şehir": ["İstanbul", "Ankara", "İzmir", "Bursa"],
    "Maaş": [50000, 60000, 45000, 52000]
}

df = pd.DataFrame(veri)
print("Tablo (DataFrame):")
print(df)

print("\n--- 2. VERİ SEÇME VE FİLTRELEME ---")
# Sadece bir sütun seçme:
isimler = df["İsim"]
print(f"Sadece İsimler:\n{isimler}")

# Koşullu Seçim (Filtreleme):
# Yaşı 25'ten büyük olanları getir:
yasli_calisanlar = df[df["Yaş"] > 25]
print(f"\nYaşı 25'ten Büyük Olanlar:\n{yasli_calisanlar}")

print("\n--- 3. YENİ SÜTUN EKLEME ---")
# Maaşa %10 Zam yapalım:
df["Yeni Maaş"] = df["Maaş"] * 1.10
print("Zamlı Tablo:")
print(df)

print("\n--- 4. ÖZET BİLGİLER ---")
# Veri hakkında istatistiksel özet:
print(df.describe())
