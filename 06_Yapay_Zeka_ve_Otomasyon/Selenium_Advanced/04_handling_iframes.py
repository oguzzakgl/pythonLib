from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def handling_iframes_practice():
    print("🚀 Tarayıcı başlatılıyor...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        # iFrame pratik sitemize gidelim
        url = "https://the-internet.herokuapp.com/iframe"
        print(f"🌐 {url} adresine gidiliyor...")
        driver.get(url)
        
        # 1. Ana sayfadaki başlığı okuyalım (Sorunsuz okuruz çünkü en dıştayız)
        h3_baslik = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
        print(f"🏠 Ana Sayfadaki Başlık: {h3_baslik}")
        
        # 2. iFrame GİRİŞ İŞLEMİ (Çelik kasaya giriyoruz)
        print("🚪 iFrame (İç Sayfa) içerisine giriliyor...")
        
        # Sitedeki iFrame'in özel bir ID'si var: "mce_0_ifr"
        # İki adımlı güvenli yöntemi kullanalım: Önce elementi bul, sonra içine switch_to ol.
        iframe_elementi = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
        driver.switch_to.frame(iframe_elementi)
        
        # 3. iFrame İçerisindeki Elementlerle Etkileşim
        # iFrame'in içinde bir metin editörü (p etiketi) var.
        editor = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
        
        # İçindeki hazır yazıyı silelim ve kendi yazımızı yazalım
        editor.clear()
        time.sleep(1)
        
        gonderilecek_yazi = "Merhaba! Bu yazı dışarıdan, iFrame'in içine Selenium tarafından sızarak yazılmıştır! 🎉"
        print(f"✍️ İçeriye yazı yazılıyor: '{gonderilecek_yazi}'")
        editor.send_keys(gonderilecek_yazi)
        time.sleep(3)
        
        # 4. iFrame'den ÇIKIŞ İŞLEMİ (Ana sayfaya geri dön)
        print("🚪 iFrame'den çıkılıyor, Ana Sayfaya (Default Content) dönülüyor...")
        driver.switch_to.default_content()
        
        # Ana sayfaya döndüğümüzü kanıtlamak için en dıştaki footer (sayfa altı) yazısını okuyalım
        footer_yazisi = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@style='text-align: center;']"))).text
        print(f"✅ Başarıyla ana sayfaya dönüldü! En alt yazı: {footer_yazisi}")
        
        time.sleep(2)

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        
    finally:
        print("🧹 Tarayıcı tamamen kapatılıyor...")
        driver.quit()

if __name__ == "__main__":
    handling_iframes_practice()

# ÖZET:
# - Bir element sayfanın içinde görünse de kodda bulunamıyorsa büyük ihtimalle bir <iframe> içindedir.
# - İçeri girmek için: driver.switch_to.frame(iframe_elementi)
# - Çıkmak için: driver.switch_to.default_content()
