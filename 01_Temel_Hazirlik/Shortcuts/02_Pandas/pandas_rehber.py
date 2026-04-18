# 🐼 Pandas Rehberi (Gerçek Veri Seti İle)
# Ortak Veri Seti: ../ortak_veri.csv

import pandas as pd
import os

# Dosya yolunu belirleyelim
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'ortak_veri.csv')

print(f"--- VERİ OKUNUYOR: {csv_path} ---")

# ==========================================
# 1. CSV Okuma
# ==========================================
df = pd.read_csv(csv_path)

print("\n--- Veri Önizleme ---")
print(df.head())

print("\n--- Veri Bilgisi ---")
print(df.info())


# ==========================================
# 2. Veri Manipülasyonu
# ==========================================
# Yeni Sütun Ekleme: Toplam Tutar
df['Toplam_Tutar'] = df['Fiyat'] * df['Adet']

# Tarihi Datetime'a Çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])
df['Ay'] = df['Tarih'].dt.month_name()

print("\n--- Yeni Sütunlar Eklendi ---")
print(df[['Urun', 'Fiyat', 'Adet', 'Toplam_Tutar', 'Ay']].head())


# ==========================================
# 3. İleri Analiz ve Gruplama
# ==========================================
print("\n--- Şehirlere Göre Ciro Analizi ---")
sehir_ciro = df.groupby('Sehir')['Toplam_Tutar'].sum().sort_values(ascending=False)
print(sehir_ciro)

print("\n--- Kategori Bazlı Ortalama Fiyat ---")
kategori_analiz = df.groupby('Kategori')['Fiyat'].mean()
print(kategori_analiz)


# ==========================================
# 4. Filtreleme
# ==========================================
print("\n--- Filtreleme: İstanbul'daki Elektronik Satışları ---")
filtre = (df['Sehir'] == 'Istanbul') & (df['Kategori'] == 'Elektronik')
istanbul_elektronik = df[filtre]
print(istanbul_elektronik[['Tarih', 'Urun', 'Toplam_Tutar']])
