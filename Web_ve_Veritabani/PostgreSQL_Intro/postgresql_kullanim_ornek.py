from sqlalchemy.orm import Session
import sys
import os

# CoinMind klasöründeki database.py'ye erişmek için yolu ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'CoinMind')))

from database import SessionLocal, engine, MarketData, User, init_db

# 1. Önce tabloların oluştuğundan emin olalım
init_db()

# 2. Veritabanı ile konuşacak bir "Oturum" (Session) başlatalım
db = SessionLocal()

print("--- PostgreSQL Kullanım Demosu Başlıyor ---\n")

# --- VERİ EKLEME (INSERT) ---
print("1. Yeni Kullanıcı Ekleniyor...")
# Yeni bir kullanıcı nesnesi oluşturuyoruz
yeni_kullanici = User(username="oguz_hoca", password="gizlisifre123")

# Veriyi oturuma ekle ve kaydet (commit)
try:
    db.add(yeni_kullanici)
    db.commit()
    print("✅ Kullanıcı eklendi!")
except Exception as e:
    db.rollback() # Hata olursa işlemi geri al
    print(f"⚠️ Kullanıcı zaten var veya hata: {e}")

print("\n2. Market Verisi Ekleniyor...")
# Bitcoin verisi ekleyelim
btc_veri = MarketData(symbol="BTC/USDT", price=45000.50, volume=120.5)
eth_veri = MarketData(symbol="ETH/USDT", price=3200.00, volume=500.2)

db.add(btc_veri)
db.add(eth_veri)
db.commit()
print("✅ Bitcoin ve Ethereum verileri eklendi!")


# --- VERİ OKUMA (SELECT) ---
print("\n3. Veriler Okunuyor...")

# Tüm market verilerini çekelim
veriler = db.query(MarketData).all()

print(f"\nToplam {len(veriler)} adet veri bulundu:")
for veri in veriler:
    print(f"💰 {veri.symbol}: ${veri.price} (Hacim: {veri.volume}) - ID: {veri.id}")

# --- TEKİL VERİ BULMA (FILTER) ---
print("\n4. Filtreleme Yapılıyor...")
bulunan_user = db.query(User).filter(User.username == "oguz_hoca").first()
if bulunan_user:
    print(f"👤 Bulunan Kullanıcı: {bulunan_user.username} (ID: {bulunan_user.id})")

# İşimiz bitince oturumu kapatalım
db.close()
print("\n--- Demo Tamamlandı ---")

# �ZET: Daha profesyonel ve �l�eklenebilir bir veritaban� olan PostgreSQL ile SQLAlchemy (ORM) k�t�phanesini kullanarak; kullan�c� ve piyasa verilerini nesne y�nelimli bir yakla��mla nas�l y�netece�imizi ��reniyoruz.
