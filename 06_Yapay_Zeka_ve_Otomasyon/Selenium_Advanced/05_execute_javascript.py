from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def javascript_executor_practice():
    print("🚀 Tarayıcı başlatılıyor...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Uzun ve aşağı kaydırma (scroll) yapabileceğimiz bir sayfaya gidelim
        url = "https://the-internet.herokuapp.com/large"
        print(f"🌐 {url} adresine gidiliyor...")
        driver.get(url)
        time.sleep(2)

        # 1. TEMEL KULLANIM: Sayfanın başlığını JavaScript ile alalım
        print("\n1️⃣ JS ile sayfa başlığı alınıyor...")
        sayfa_basligi = driver.execute_script("return document.title;")
        print(f"   ✅ Site başlığı '{sayfa_basligi}'")
        
        # 2. KAYDIRMA: Sayfayı belirli bir Pixel kadar aşağı kaydıralım
        print("\n2️⃣ Sayfa 500 piksel aşağı kaydırılıyor...")
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2) # Kaydırmayı görmek için bekle
        
        # 3. KAYDIRMA: Sayfanın en altına kadar gidelim
        print("\n3️⃣ Sayfanın EN ALTINA kaydırılıyor...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # 4. ELEMENTE KAYDIRMA: Sayfanın üstlerinde kalan özel bir tablo hücresini bulup oraya geri çıkalım
        print("\n4️⃣ Belirli bir elementin olduğu yere (Yukarıya) geri dönülüyor...")
        # '4.2' yazan hücreyi bul
        hedef_hücre = driver.find_element(By.ID, "sibling-2.2") 
        # JavaScript yardımıyla o elementi ekranın tam ortasına veya üstüne gelecek şekilde kaydır
        driver.execute_script("arguments[0].scrollIntoView(true);", hedef_hücre)
        
        print(f"   🎯 Gösterilen hücrenin içindeki yazı: '{hedef_hücre.text}'")
        time.sleep(3)
        

        # (Ekstra Pratik) Başka bir siteye gidip İnatçı Butona tıklamayı görelim:
        url2 = "https://login.yahoo.com/" # Görünmez katmanların bol olduğu bir site
        print(f"\n🌐 {url2} adresine gidiliyor (Zorla Tıklama Testi)...")
        driver.get(url2)
        
        # Yahoo'da "Create an account" (Hesap Oluştur) butonunu bulalım
        hesap_olustur_btn = wait.until(EC.presence_of_element_located((By.ID, "createacc")))
        
        print("   💪 JS ile butona ZORLA tıklanıyor...")
        # Normal click() hata verebilirdi, biz JS ile direkt sisteme tıklattırıyoruz.
        driver.execute_script("arguments[0].click();", hesap_olustur_btn)
        
        time.sleep(4)
        print("   ✅ Yeni sayfaya başarıyla geçildi!")


    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        
    finally:
        print("\n🧹 Tarayıcı tamamen kapatılıyor...")
        driver.quit()

if __name__ == "__main__":
    javascript_executor_practice()

# ÖZET:
# - B Planımız her zaman JavaScript çalıştırmaktır. Hata veren elementler için cankurtarandır.
# - Kod: driver.execute_script("js_kodu_veya_komut", opsiyonel_element)
