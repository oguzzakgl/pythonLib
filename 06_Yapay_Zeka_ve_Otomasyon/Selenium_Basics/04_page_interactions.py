from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
SELENIUM SAYFA ETKİLEŞİMLERİ (SCROLL & SELECT)
---------------------------------------------
Bu script, sayfada aşağı kaydırma yapmayı ve açılır menülerden
(dropdown) seçim yapmayı gösterir.
"""

def page_interactions_practice():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        # 🟢 Örnek 1: Sayfa Kaydırma (Scroll)
        print("🌐 GitHub Trending sayfasına gidiliyor...")
        driver.get("https://github.com/trending")
        
        # Sayfayı yavaş yavaş kaydıralım (Görsel efekt için)
        for i in range(3):
            print(f"📄 Aşağı kaydırılıyor... (Adım {i+1})")
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            
        # 🟢 Örnek 2: Select Menüsü (Dropdown)
        # Pratik için eBay'in kategori seçimi menüsünü kullanalım
        print("\n🌐 eBay sayfasına gidiliyor...")
        driver.get("https://www.ebay.com")
        
        # Kategori dropdown'ını bulalım (<select id="gh-cat">)
        dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "gh-cat")))
        dropdown = Select(dropdown_element)
        
        # Farklı yöntemlerle seçim yapalım
        print("🖱️ Kategori: 'Books' seçiliyor (Visible Text)...")
        dropdown.select_by_visible_text("Books")
        time.sleep(2)
        
        print("🖱️ Kategori: Index 5 seçiliyor...")
        dropdown.select_by_index(5)
        time.sleep(2)
        
        print("🖱️ Kategori: 'Art' seçiliyor (Value)...")
        dropdown.select_by_value("550") # Art kategorisinin value'su genelde 550'dir
        
        print("\n✅ Sayfa etkileşimleri başarıyla simüle edildi!")
        time.sleep(3)

    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")
    
    finally:
        driver.quit()

# ÖZET: Sadece tıklamak yetmez; bazen JavaScript kullanarak sayfayı aşağı kaydırmamız (Scroll) 
# veya açılır menülerden (Select sınıfı) seçim yapmamız gerekir.
        print("🧹 Tarayıcı kapatıldı.")

if __name__ == "__main__":
    page_interactions_practice()
