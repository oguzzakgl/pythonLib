# 🌊 Seaborn Rehberi (Gerçek Veri Seti İle)
# Ortak Veri Seti: ../ortak_veri.csv

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# Veriyi Yükle
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'ortak_veri.csv')
df = pd.read_csv(csv_path)

# Veri Hazırlığı
df['Toplam_Tutar'] = df['Fiyat'] * df['Adet']

print("Grafikler oluşturuluyor...")
sns.set_theme(style="darkgrid")

# ==========================================
# 1. Barplot (Şehir ve Kategori Analizi)
# ==========================================
plt.figure(figsize=(10, 6))
# Şehirlere göre fiyat ortalaması, her barın içinde Kategori kırılımı (hue)
sns.barplot(data=df, x="Sehir", y="Fiyat", hue="Kategori", errorbar=None)
plt.title("Şehir ve Kategoriye Göre Ortalama Ürün Fiyatları")
plt.show()


# ==========================================
# 2. Boxplot (Fiyat Dağılımı)
# ==========================================
plt.figure(figsize=(8, 6))
# Fiyatların dağılımını ve varsa aykırı değerleri gösterir
sns.boxplot(data=df, x="Kategori", y="Fiyat", palette="Set2")
plt.title("Kategori Bazlı Fiyat Dağılımı")
plt.show()


# ==========================================
# 3. Heatmap (Korelasyon)
# ==========================================
plt.figure(figsize=(8, 6))
# Sadece sayısal sütunları al
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_df.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Değişkenler Arası Korelasyon")
plt.show()
