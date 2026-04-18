# 📊 Matplotlib Rehberi (Gerçek Veri Seti İle)
# Ortak Veri Seti: ../ortak_veri.csv

import matplotlib.pyplot as plt
import pandas as pd
import os

# Veriyi Pandas ile okuyup hazırlayalım
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'ortak_veri.csv')
df = pd.read_csv(csv_path)

# İşlemler
df['Toplam_Tutar'] = df['Fiyat'] * df['Adet']
# Şehir bazlı toplam ciroyu hesapla
sehir_veri = df.groupby('Sehir')['Toplam_Tutar'].sum()

print("Grafikler oluşturuluyor...")
plt.style.use('dark_background')

# ==========================================
# 1. Sütun Grafiği (Şehir Ciroları)
# ==========================================
plt.figure(figsize=(10, 6))

# x: Şehir İsimleri (sehir_veri.index), y: Cirolar (sehir_veri.values)
plt.bar(sehir_veri.index, sehir_veri.values, color=['#ff9999', '#66b3ff', '#99ff99'])

plt.title("Şehirlere Göre Toplam Ciro")
plt.xlabel("Şehirler")
plt.ylabel("Ciro (TL)")
plt.grid(axis='y', alpha=0.3)
plt.show()


# ==========================================
# 2. Pasta Grafiği (Kategori Dağılımı)
# ==========================================
kategori_veri = df['Kategori'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(kategori_veri, labels=kategori_veri.index, autopct='%1.1f%%', startangle=140)
plt.title("İşlem Sayısına Göre Kategori Dağılımı")
plt.show()


# ==========================================
# 3. Çizgi Grafiği (Zaman İçindeki Satış)
# ==========================================
df['Tarih'] = pd.to_datetime(df['Tarih'])
tarih_veri = df.groupby('Tarih')['Toplam_Tutar'].sum()

plt.figure(figsize=(10, 5))
plt.plot(tarih_veri.index, tarih_veri.values, marker='o', linestyle='-', color='cyan')
plt.title("Günlük Satış Trendi")
plt.xticks(rotation=45) # Tarihleri eğik yaz
plt.tight_layout()
plt.show()
