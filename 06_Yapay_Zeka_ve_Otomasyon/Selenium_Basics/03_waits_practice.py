from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
SELENIUM WAITS (BEKLEMELER) UYGULAMASI
-------------------------------------
Bu script, Explicit Wait kullanarak elementlerin yüklenmesini
nasıl "akıllı" bir şekilde bekleyeceğimizi gösterir.
"""

def waits_practice():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # 1. Bekleme nesnesini oluşturuyoruz (Max 15 saniye bekleyecek)
    wait = WebDriverWait(driver, 15)
    
    try:
        # Örnek olarak Google üzerinde deneyelim
        url = "https://www.google.com"
        driver.get(url)
        
        # Çerez onayı (varsa) bekleyelim ve tıklayalım
        # Not: Türkiye'de genellikle çıkmaz ama çıkarsa hata almamak için:
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "L2AGLb")))
            accept_button.click()
            print("🍪 Çerezler kabul edildi.")
        except:
            print("ℹ️ Çerez ekranı çıkmadı, devam ediliyor.")

        # 2. Arama kutusunun görünür olmasını bekle (Explicit Wait)
        # Google arama kutusu name="q" özelliğine sahiptir
        search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
        print("✅ Arama kutusu görünür oldu.")
        
        search_box.send_keys("Selenium Python Documentation")
        search_box.submit() # Enter tuşu yerine submit() kullanabiliriz
        
        # 3. Sonuçların gelmesini bekleyelim
        # İlk sonucun başlığını (h3 etiketi) bekleyelim
        first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        print(f"🎯 İlk Sonuç Bulundu: {first_result.text}")
        
        print("\n🚀 Explicit Wait sayesinde hiçbir 'time.sleep' kullanmadan senkronizasyonu sağladık!")
        time.sleep(3) # Sadece sonucu görmen için kısa bir mola

    except Exception as e:
        print(f"❌ Bekleme sırasında hata oluştu veya süre doldu: {e}")
    
    finally:
        driver.quit()

# ÖZET: Dinamik web sitelerinde elementlerin yüklenmesini sabırla beklemeyi öğreniyoruz. 
# NoSuchElementException hatasından kurtulmanın en profesyonel yolu 'WebDriverWait' (Explicit Wait) yapısıdır.
        print("🧹 Tarayıcı kapatıldı.")

if __name__ == "__main__":
    waits_practice()
