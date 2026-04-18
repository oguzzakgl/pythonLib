from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

"""
İLK SELENIUM SCRIPTİ: Tarayıcı Açma ve Temel Kontroller
------------------------------------------------------
Bu script, Selenium'un çalışma mantığını en basit haliyle gösterir.
"""

def selenium_hello_world():
    try:
        print("🚀 Selenium başlatılıyor...")
        
        # Chrome tarayıcısını başlatıyoruz
        # Not: Selenium 4.6+ sürümlerinde Driver otomatik olarak indirilir.
        driver = webdriver.Chrome()
        
        # Tarayıcı penceresini tam ekran yapalım
        driver.maximize_window()
        
        # Hedef siteye gidelim
        target_url = "https://github.com/oguzzakgl"
        print(f"🌐 {target_url} adresine gidiliyor...")
        driver.get(target_url)
        
        # Sayfa başlığını alalım
        page_title = driver.title
        print(f"✅ Sayfa başarıyla açıldı! Başlık: {page_title}")
        
        # 5 saniye bekleyelim (Gözlemlemek için)
        print("⏳ 5 saniye boyunca sayfayı inceleyebilirsiniz...")
        time.sleep(5)
        
        # Tarayıcıyı kapatalım
        print("🧹 Tarayıcı kapatılıyor...")
        driver.quit()
        
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")

if __name__ == "__main__":
    selenium_hello_world()

# ÖZET: Selenium yolculuğunun ilk adımı. Tarayıcıyı nasıl açacağımızı, 
# bir siteye nasıl gideceğimizi ve temel temizlik işlemini (quit) öğreniyoruz.
