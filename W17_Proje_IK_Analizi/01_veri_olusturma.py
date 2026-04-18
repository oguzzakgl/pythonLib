import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# --- 1. AYARLAR ---
fake = Faker('tr_TR')  # Türkçe isimler
random.seed(42)        # Sonuçlar hep aynı çıksın
np.random.seed(42)

# --- 2. SABİT LİSTELER ---
DEPARTMANLAR = ['IT', 'İnsan Kaynakları', 'Finans', 'Satış', 'Pazarlama', 'Üretim']
EGITIM_SEVIYELERI = ['Lise', 'Lisans', 'Yüksek Lisans', 'Doktora']

# --- 3. VERİ ÜRETİMİ (1000 Kişi) ---
calisan_listesi = []

print("⏳ Veri üretiliyor, lütfen bekleyin...")

for _ in range(1000):
    # Kişisel Bilgiler
    isim = fake.name()
    sehir = fake.city()
    yas = random.randint(22, 60)
    
    # İş Bilgileri
    departman = random.choice(DEPARTMANLAR)
    egitim = random.choice(EGITIM_SEVIYELERI)
    tecrube = max(0, yas - 22 - random.randint(0, 5)) # Yaş - 22'den en fazla 5 yıl az olabilir
    
    # Maaş Hesaplama (MANTIKLI OLSUN DİYE)
    base_maas = 25000
    maas = base_maas + (tecrube * 2500) # Her yıl için +2500 TL
    
    if departman in ['IT', 'Finans']: # IT ve Finans +%20 primli
        maas = maas * 1.2
        
    if egitim in ['Yüksek Lisans', 'Doktora']: # Yüksek lisans +3000 TL
        maas = maas + 3000
        
    # Performans (Çan eğrisi ile 1-100 arası dağıt)
    performans = int(np.random.normal(70, 15)) # Ortalaması 70, sapması 15
    performans = max(1, min(100, performans))  # 0 veya 100'ü geçmesin
    
    # Listeye Ekle
    calisan_listesi.append({
        'Isim': isim,
        'Sehir': sehir,
        'Yas': yas,
        'Departman': departman,
        'Egitim': egitim,
        'Tecrube': tecrube,
        'Maas': int(maas),
        'Performans': performans
    })

# --- 4. KAYDETME ---
df = pd.DataFrame(calisan_listesi)


current_dir = os.path.dirname(os.path.abspath(__file__))
dosya_adi = os.path.join(current_dir, 'ik_performans.csv')

df.to_csv(dosya_adi, index=False)

print("\n✅ Veri başarıyla üretildi!")
print(f"📂 Dosya Yolu: {dosya_adi}")
print("-" * 30)
print(df.head()) # İlk 5 satırı göster
