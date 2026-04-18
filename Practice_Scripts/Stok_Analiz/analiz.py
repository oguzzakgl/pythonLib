# Veri Analizi ve Raporlama (Pandas & SQL & Matplotlib)
import pandas as pd
import numpy as np   
import sqlite3
import matplotlib.pyplot as plt # Çizim kütüphanesini ekledik (Kısa adı: plt)

def verileri_getir():
    con = sqlite3.connect("stok.db")
    df = pd.read_sql("SELECT * FROM urunler", con)
    con.close()
    return df

print("--- 1. VERİ YÜKLENİYOR ---")
df = verileri_getir()
print(df)

print("\n--- 2. FİNANSAL ANALİZ ---")
# Yeni Sütun Ekleme: Toplam Değer = Fiyat * Stok
df["Toplam_Deger"] = df["fiyat"] * df["stok"]
print(df)

toplam_stok_degeri = df["Toplam_Deger"].sum()
print(f"\nDepodaki Ürünlerin Toplam Değeri: {toplam_stok_degeri} TL")

print("\n--- 3. KRİTİK STOK RAPORU ---")
# Stoğu 20'den az olanları bul
kritik_seviye = 20
kritik_urunler = df[df["stok"] < kritik_seviye]

if not kritik_urunler.empty:
    print(f"DİKKAT! Stok sayısı {kritik_seviye}'in altında olan ürünler:")
    print(kritik_urunler[["ad", "stok"]]) # Sadece ad ve stok sütununu göster
    
    # Raporu kaydet
    kritik_urunler.to_csv("kritik_stok_raporu.csv", index=False)
    print("-> 'kritik_stok_raporu.csv' dosyası oluşturuldu.")
else:
    print("Harika! Kritik seviyede ürün yok.")

print("\n--- 4. GÖRSELLEŞTİRME (Matplotlib) ---")
# Matplotlib Kullanımı:
# 1. plt.bar(x_ekseni, y_ekseni) -> Çubuk grafik çizer
# 2. plt.show() -> Ekrana basar (veya savefig ile kaydeder)

try:
    plt.figure(figsize=(10, 6)) # Grafik boyutunu ayarla (Genişlik: 10, Yükseklik: 6)
    plt.bar(df["ad"], df["stok"], color="skyblue") # X: Ürün Adı, Y: Stok, Renk: Gök Mavisi
    
    plt.title("Ürün Stok Durumları") # Başlık
    plt.xlabel("Ürün Adı") # Alt etiket
    plt.ylabel("Stok Adedi") # Yan etiket
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Arka plana çizgiler ekle (Daha rahat okunsun diye)
    
    plt.savefig("stok_grafik.png") # Resmi kaydet
    print("-> 'stok_grafik.png' dosyası oluşturuldu. Klasörü kontrol et!")
    
except Exception as e:
    print(f"Grafik çizilirken hata oluştu: {e}")


# �ZET: Veritaban�ndaki stok verilerini Pandas ile analiz ederek; finansal hesaplamalar yapmay�, kritik stok raporu (CSV) olu�turmay� ve Matplotlib ile g�rselle�tirmeyi ��reniyoruz.
