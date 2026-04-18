# 03_veri_analizi.py
# Bu derste gerçek hayatta sıkça karşılaşacağımız "Kirli Veri" ile başa çıkmayı
# ve veriden anlamlı raporlar çıkarmayı (Gruplama) öğreneceğiz.

import pandas as pd
import numpy as np

print("--- 1. GERÇEKÇİ (KİRLİ) VERİ SETİ OLUŞTURMA ---")
# İçinde eksik veriler (None, np.nan) olan bir veri seti oluşturalım:
data = {
    "Departman": ["İK", "Yazılım", "Yazılım", "Pazarlama", "İK", "Yazılım", "Pazarlama"],
    "Çalışan": ["Ahmet", "Mehmet", "Ayşe", "Fatma", None, "Ali", "Veli"], # Bir isim eksik
    "Maaş": [50000, 60000, 55000, 52000, 48000, np.nan, 58000],          # Bir maaş eksik
    "Tecrübe Yıl": [3, 5, 4, 3, 2, 7, 5]
}

df = pd.DataFrame(data)
print("Ham Veri:")
print(df)
print("\nVeri Bilgisi:")
print(df.info())

print("\n--- 2. EKSİK VERİLERİ TEMİZLEME (CLEANING) ---")
# 1. Yöntem: Eksik verisi olan satırları sil (dropna)
print(f"\nEksik verileri silersek kalan satır sayısı: {len(df.dropna())}")

# 2. Yöntem: Eksik verileri doldur (fillna)
# Maaşı eksik olanlara "Departman Ortalaması" veya "Genel Ortalama" verilebilir.
# Biz şimdilik ortalama maaş atayalım:
ortalama_maas = df["Maaş"].mean()
print(f"\nOrtalama Maaş: {ortalama_maas:.2f}")

df["Maaş"] = df["Maaş"].fillna(ortalama_maas)
df["Çalışan"] = df["Çalışan"].fillna("Bilinmiyor") # İsmi olmayana 'Bilinmiyor' dedik

print("\nTemizlenmiş Veri:")
print(df)

print("\n--- 3. GRUPLAMA VE ANALİZ (GROUPBY) - EN ÖNEMLİ KISIM ---")
# "Hangi departman toplam ne kadar maaş alıyor?" sorusunun cevabı:
bolum_ozeti = df.groupby("Departman")["Maaş"].sum()
print("Departman Bazlı Toplam Maaşlar:")
print(bolum_ozeti)

print("\nDepartman Bazlı Ortalama Maaş ve Çalışan Sayısı:")
# Birden fazla işlem (aggregation) yapma:
detayli_ozet = df.groupby("Departman").agg({
    "Maaş": ["mean", "min", "max"],
    "Çalışan": "count"
})
print(detayli_ozet)

print("\n--- 4. SIRALAMA (SORTING) ---")
# Maaşa göre çoktan aza sıralama:
sirali_df = df.sort_values(by="Maaş", ascending=False)
print("Maaşa Göre Sıralı Liste:")
print(sirali_df)
