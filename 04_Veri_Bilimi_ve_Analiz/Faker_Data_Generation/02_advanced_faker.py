from faker import Faker
from faker.providers import BaseProvider
import pandas as pd
import random

# ==========================================
# İLERİ SEVİYE FAKER KULLANIMI (ADVANCED)
# ==========================================
print("--- İLERİ SEVİYE FAKER: LOKALİZASYON VE ÖZELLEŞTİRME ---\n")

# 1. Lokalizasyon (Farklı Dillerde Veri Üretme)
print("1. Çoklu Dil Desteği (Türkçe, Japonca, Almanca):")
# Aynı anda birden fazla dili destekleyen bir liste verebiliriz
fake_intl = Faker(['tr_TR', 'ja_JP', 'de_DE'])

for _ in range(3):
    print(f"Rastgele İsim: {fake_intl.name()}")
    print(f"Rastgele Ülke: {fake_intl.country()}")
    print("-" * 15)
print("-" * 30)


# 2. Unique (Benzersiz) Veri Üretimi
print("2. Unique (Benzersiz) Değerler:")
# Örneğin ID numaralarının asla çakışmaması gerekir
fake = Faker()

print("Benzersiz ID'ler:")
for _ in range(5):
    # .unique metodunu kullanarak daha önce üretilmemiş bir değer garanti edilir
    print(fake.unique.random_int(min=1000, max=1010))

# Eğer aralık biterse hata verir (1000-1010 arası sadece 11 sayı var)
# fake.unique.clear() # Resetlemek için
print("-" * 30)


# 3. Custom Provider (Kendi Sahte Veri Üreticimizi Yazma)
print("3. Custom Provider (Özel Veri Seti):")
# Faker'ın standart kütüphanesinde olmayan bir şey üretmek istiyoruz.
# Örneğin: "Rastgele Yazılım Dili" veya "Rastgele Türk Yemekleri"

class TechProvider(BaseProvider):
    def programming_language(self):
        langs = ['Python', 'Java', 'C#', 'Go', 'Rust', 'JavaScript', 'TypeScript']
        return random.choice(langs)
    
    def tech_role(self):
        roles = ['Backend Dev', 'Frontend Dev', 'AI Engineer', 'DevOps Specialist']
        return random.choice(roles)

# Provider'ı ekle
fake.add_provider(TechProvider)

print(f"Favori Dil: {fake.programming_language()}")
print(f"Rol: {fake.tech_role()}")
print(f"Favori Dil: {fake.programming_language()}")
print("-" * 30)


# 4. İlişkisel Veri Üretimi (Dummy Relational Data)
print("4. İlişkisel Veri (Şirket - Çalışan):")
# Bir kişi hem isme hem de o isme uygun bir e-postaya sahip olmalı

data = []
for _ in range(5):
    # Profil oluşturma (simple_profile çok kullanışlıdır)
    profile = fake.profile(fields=['name', 'mail', 'birthdate'])
    
    # Kendi özel alanlarımızı ekleyelim
    profile['role'] = fake.tech_role()
    profile['main_lang'] = fake.programming_language()
    
    data.append(profile)

df = pd.DataFrame(data)
print(df)
print("\nİpucu: 'fake.profile()' ile hızlıca tutarlı kullanıcı verisi oluşturabilirsiniz.")

# �ZET: Faker k�t�phanesini farkl� dillerde (T�rk�e, Japonca vb.) kullanmay�, benzersiz (unique) veriler �retmeyi ve kendi �zel veri sa�lay�c�lar�m�z� (Custom Provider) yazmay� ke�fediyoruz.
