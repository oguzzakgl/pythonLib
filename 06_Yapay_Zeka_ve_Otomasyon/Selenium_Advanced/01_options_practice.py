from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def advanced_setup():
    # 1. Option Nesnesini Oluştur
    options = Options()

    # 2. Çeşitli Ayarlar Ekle
    print("🚀 Ayarlar yapılandırılıyor...")
    options.add_argument("--headless") # Arayüzü gizle (Denemek için yorum satırına alabilirsin)
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    
    # User-Agent: Kendimizi gerçek bir kullanıcı gibi gösterelim
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    # 3. Resimleri Engelle (Hız için)
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    # 4. Driver'ı Başlat
    driver = webdriver.Chrome(options=options)

    try:
        print("🌐 Siteye gidiliyor (Headless Mod Aktif)...")
        driver.get("https://www.google.com")
        
        # Sayfa başlığını kontrol et
        print(f"✅ Sayfa Başlığı: {driver.title}")
        print(f"🕵️ Kullanılan User-Agent: {driver.execute_script('return navigator.userAgent')}")
        
        # Ekran görüntüsü al (Headless modda çalıştığımızı kanıtlayalım)
        driver.save_screenshot("google_headless.png")
        print("📸 Ekran görüntüsü kaydedildi: google_headless.png")

    finally:
        driver.quit()
        print("🧹 Tarayıcı kapatıldı.")

if __name__ == "__main__":
    advanced_setup()

# ÖZET: Gerçek projelerde tarayıcının pat diye açılması her zaman istenmez. 
# Özellikle sunucularda veya botun fark edilmemesi gereken durumlarda 'Options' kullanarak 
# tarayıcıyı gizli (headless) modda çalıştırırız.
