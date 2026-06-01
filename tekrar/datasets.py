import numpy as np
import pandas as pd

np.random.seed(42)

# 5000 satırlık satış verisi
n = 5000

veri = {
    "tarih": pd.date_range("2025-01-01", periods=n, freq="h"),
    "urun_kodu": np.random.choice(["URUN_A", "URUN_B", "URUN_C", "URUN_D"], n),
    "kategori": np.random.choice(["Elektronik", "Giyim", "Mutfak"], n),
    "adet": np.random.randint(1, 20, n),
    "birim_fiyat": np.round(np.random.uniform(10, 500, n), 2),
    "musteri_sehir": np.random.choice(["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"], n),
    "musteri_yasi": np.random.randint(18, 70, n),
    "odeme_tipi": np.random.choice(["Kredi Kartı", "Nakit", "Havale"], n, p=[0.6, 0.3, 0.1]),
}

df = pd.DataFrame(veri)

# Toplam satış sütunu ekle
df["toplam_tutar"] = df["adet"] * df["birim_fiyat"]

# Bilerek eksik veri ekle (%5)
for sutun in ["musteri_yasi", "odeme_tipi", "birim_fiyat"]:
    eksik_idx = np.random.choice(df.index, size=int(n * 0.05), replace=False)
    df.loc[eksik_idx, sutun] = np.nan

# Bilerek hatalı veri ekle
df.loc[np.random.choice(df.index, 20), "adet"] = -5  # negatif adet
df.loc[np.random.choice(df.index, 10), "birim_fiyat"] = 0  # sıfır fiyat

# Kaydet
df.to_csv("satis_verisi.csv", index=False)
print("✅ satis_verisi.csv oluşturuldu.")
print(f"   {n} satır, {len(df.columns)} sütun")
print(f"   Eksik veri: {df.isna().sum().sum()} hücre")