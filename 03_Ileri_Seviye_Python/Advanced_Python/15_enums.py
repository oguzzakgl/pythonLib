# Konu: Enum (Enumeration)
# Amaç: Sabit seçenekleri (Renkler, Roller, Durumlar) isimlerle yönetmek.
# Neden? "Magic String" (rastgele metin) kullanmaktan kaçınmak ve hataları önlemek için.

from enum import Enum, auto

# ----------------------------------------
# 1. TEMEL ENUM TANIMLAMA
# ----------------------------------------
class KullaniciRolu(Enum):
    # İsim = Değer
    ADMIN = 1
    EDITOR = 2
    GUEST = 3

# ----------------------------------------
# 2. STRING ENUM (FastAPI'de çok kullanılır!)
# ----------------------------------------
class SiparisDurumu(str, Enum):
    BEKLIYOR = "bekliyor"
    ONAYLANDI = "onaylandi"
    KARGOYA_VERILDI = "kargoda"
    TESLIM_EDILDI = "teslim"
    IPTAL = "iptal"

def siparis_kontrol(durum: SiparisDurumu):
    # Tip güvenliği sağlar. Yanlış bir string girerseniz ide uyarır.
    if durum == SiparisDurumu.KARGOYA_VERILDI:
        print("🚚 Siparişiniz yola çıktı!")
    elif durum == SiparisDurumu.TESLIM_EDILDI:
        print("✅ Sipariş teslim edildi.")
    else:
        print(f"Sipariş durumu: {durum.value}")

if __name__ == "__main__":
    print(f"Rol: {KullaniciRolu.ADMIN} - Değer: {KullaniciRolu.ADMIN.value}")
    
    # Doğru Kullanım
    benim_siparisim = SiparisDurumu.KARGOYA_VERILDI
    siparis_kontrol(benim_siparisim)
    
    # Neden Enum?
    # siparis_kontrol("kargoda") # Bu çalışır ama IDE ne yazacağını söylemez.
    # siparis_kontrol(SiparisDurumu.KARGOYA_VERILDI) # IDE sana seçenekleri sunar (Admin, Guest vb.)
    
    # Listeleyelim
    print("\n--- Mevcut Durumlar ---")
    for d in SiparisDurumu:
        print(f"- {d.name} -> {d.value}")

# �ZET: Renkler, roller veya sipari� durumlar� gibi belirli sabit se�enekleri isimlerle y�neterek hata pay�n� azaltan Enum yap�s�n� ��reniyoruz.
