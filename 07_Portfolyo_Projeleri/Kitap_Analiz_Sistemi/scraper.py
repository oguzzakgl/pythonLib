import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
🚀 Gelişmiş Kitap Veri Botu (Scraper)
-----------------------------------
Bu bot, 'Books to Scrape' sitesindeki tüm sayfaları (veya belirli sayıda sayfayı) gezer,
her kitabın adını, fiyatını, yıldız puanını ve kategorisini çeker.
"""

class BookScraper:
    def __init__(self, max_pages=5):
        self.base_url = "https://books.toscrape.com/"
        self.max_pages = max_pages
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.scraped_data = []

    def get_rating(self, book_element):
        # Yıldız puanları class isminde yazılı: "star-rating Three"
        rating_classes = book_element.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
        # 'star-rating' kısmını atıp sadece kelimeyi alıyoruz
        return rating_classes.replace("star-rating ", "")

    def scrape(self):
        try:
            print(f"📡 Bot başlatıldı. İlk {self.max_pages} sayfa taranacak...")
            
            for page in range(1, self.max_pages + 1):
                url = f"{self.base_url}catalogue/page-{page}.html"
                print(f"🌐 Sayfa {page} taranıyor: {url}")
                self.driver.get(url)
                
                # Kitap kartlarını bul
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_pod")))
                books = self.driver.find_elements(By.CLASS_NAME, "product_pod")
                
                for book in books:
                    title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
                    price = book.find_element(By.CLASS_NAME, "price_color").text
                    rating = self.get_rating(book)
                    stock = book.find_element(By.CLASS_NAME, "instock").text.strip()
                    
                    self.scraped_data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Stock": stock,
                        "Page": page
                    })
                
                print(f"✅ Sayfa {page} tamamlandı. Toplam veri: {len(self.scraped_data)}")
                time.sleep(1) # Siteyi yormamak için kısa bir mola

            self.save_data()

        except Exception as e:
            print(f"❌ Scraper hatası: {e}")
        finally:
            self.driver.quit()
            print("🧹 Tarayıcı kapatıldı.")

    def save_data(self):
        # Scriptin olduğu dizini baz alıyoruz
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        df = pd.DataFrame(self.scraped_data)
        file_path = os.path.join(data_dir, "raw_books_data.csv")
        df.to_csv(file_path, index=False, encoding="utf-8-sig")
        print(f"\n💾 Veriler başarıyla kaydedildi: {file_path}")
        print(df.head())

if __name__ == "__main__":
    # Test amaçlı 3 sayfa çekelim (Toplam 60 kitap)
    scraper = BookScraper(max_pages=3)
    scraper.scrape()

# ÖZET: Portfolyo projesinin kalbi. Çok sayfalı veri çekme, detaylı ayıklama 
# ve ham veriyi CSV olarak kaydetme süreçlerini yöneten gelişmiş bottur.
