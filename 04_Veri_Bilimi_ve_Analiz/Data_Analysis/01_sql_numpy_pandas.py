# KONU: SQL, NumPy ve Pandas Entegrasyonu
# AmaÃ§: 
# 1. SQL: Veriyi saklamak (Depo)
# 2. NumPy: SayÄ±sal hesaplama yapmak (Hesap Makinesi)
# 3. Pandas: Veriyi raporlamak ve gÃ¶stermek (Excel)

import sqlite3
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# ADIM 1: SQL (BACKEND) - Veri Ãœretme
# ---------------------------------------------------------
print("--- 1. SQL ADIMI: VeritabanÄ± OluÅŸturuluyor ---")

# GeÃ§ici (RAM'de) bir veritabanÄ± kuralÄ±m
baglanti = sqlite3.connect(":memory:") 
cursor = baglanti.cursor()

# Tablo YapÄ±sÄ±
cursor.execute("CREATE TABLE sinavlar (ogrenci_adi TEXT, notu INTEGER)")

# Veri Ekleyelim
veriler = [
    ("Ahmet", 85),
    ("AyÅŸe", 90),
    ("Mehmet", 45),
    ("Fatma", 60),
    ("Ali", 100)
]
cursor.executemany("INSERT INTO sinavlar VALUES (?, ?)", veriler)
baglanti.commit()
print("âœ… Veriler SQL'e kaydedildi.")

# ---------------------------------------------------------
# ADIM 2: PANDAS (ANALÄ°Z) - Veriyi Ã‡ekme
# ---------------------------------------------------------
print("\n--- 2. PANDAS ADIMI: Veri SQL'den Ã‡ekiliyor ---")

# SQL'den veriyi alÄ±p Pandas DataFrame'e (Tabloya) Ã§evirir
df = pd.read_sql("SELECT * FROM sinavlar", baglanti)

print("Pandas Tablosu:")
print(df)

# ---------------------------------------------------------
# ADIM 3: NUMPY (MATEMATÄ°K) - Hesaplama
# ---------------------------------------------------------
print("\n--- 3. NUMPY ADIMI: Ä°statistiksel Hesaplama ---")

notlar = df["notu"].values # Pandas sÃ¼tununu NumPy dizisine Ã§evir

ortalama = np.mean(notlar)
standart_sapma = np.std(notlar)
en_yuksek = np.max(notlar)

print(f"SÄ±nÄ±f OrtalamasÄ±:  {ortalama}")
print(f"Standart Sapma:    {standart_sapma:.2f}")
print(f"En YÃ¼ksek Not:     {en_yuksek}")

# ---------------------------------------------------------
# BONUS: Pandas ile Filtreleme
# ---------------------------------------------------------
print("\n--- BONUS: GeÃ§enler (Notu 50'den BÃ¼yÃ¼k) ---")
gecenler = df[df["notu"] > 50]
print(gecenler)

# ÖZET: Veri biliminin üç ayaðý olan SQL (saklama), Pandas (analiz) ve NumPy (matematik) arasýndaki veri geçiþlerini ve bu teknolojilerin nasýl uyum içinde çalýþtýðýný öðreniyoruz.
