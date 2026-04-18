from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

"""
SELENIUM MINI PROJE: WEB SCRAPING
---------------------------------
Hedef: 'Books to Scrape' sitesinden kitap isimlerini ve fiyatlarını çekmek,
ardından bu verileri bir Pandas DataFrame'e aktarıp kaydetmek.
"""

def scraping_mini_project():
    # Tarayıcı ayarları (Opsiyonel: Headless mod - Tarayıcıyı görmeden çalıştırmak için)
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    scraped_data = []
    
    try:
        url = "https://books.toscrape.com/"
        print(f"🌐 {url} adresine bağlanılıyor...")
        driver.get(url)
        
        # 1. Kitapların listelendiği ana kapsayıcıyı bekle
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_pod")))
        
        # 2. Sayfadaki tüm kitap kartlarını bul
        books = driver.find_elements(By.CLASS_NAME, "product_pod")
        print(f"📚 Sayfada {len(books)} adet kitap bulundu. Veriler çekiliyor...\n")
        
        # 3. Her kitap kartı üzerinde döngü kur ve bilgileri ayıkla
        for book in books:
            # Kitap adı (h3 etiketinin içindeki a etiketinin title özelliği)
            title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
            
            # Fiyat (class="price_color")
            price = book.find_element(By.CLASS_NAME, "price_color").text
            
            # Stok durumu (class="instock availability")
            stock = book.find_element(By.CLASS_NAME, "instock").text.strip()
            
            print(f"📖 {title[:30]}... | 💰 {price} | ✅ {stock}")
            
            # Veriyi sözlük yapısında listeye ekle
            scraped_data.append({
                "Kitap Adı": title,
                "Fiyat": price,
                "Stok Durumu": stock
            })
            
        # 4. Verileri Pandas ile kaydetme
        print("\n💾 Veriler işleniyor ve kaydediliyor...")
        df = pd.DataFrame(scraped_data)
        
        # CSV ve Excel olarak kaydet
        df.to_csv("kitap_listesi.csv", index=False, encoding="utf-8-sig")
        print("✅ 'kitap_listesi.csv' başarıyla oluşturuldu.")
        
        time.sleep(3)

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
    
    finally:
        driver.quit()
        print("🧹 Tarayıcı kapatıldı.")

if __name__ == "__main__":
    scraping_mini_project()

# ÖZET: Öğrendiğimiz her şeyi birleştirip gerçek bir siteden birden fazla veriyi 
# çekip Pandas ile listelediğimiz ilk canlı uygulama örneğimizdir.
