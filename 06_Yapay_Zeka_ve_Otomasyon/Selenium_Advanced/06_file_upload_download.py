import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def file_upload_download_practice():
    print("🚀 Tarayıcı ayarları yapılandırılıyor...")
    
    # İndirilecek dosyalar için özel bir klasör ayarlayalım
    # Mevcut python dosyasının olduğu dizine 'İndirilen_Dosyalar' adında bir klasör rotası belirleyelim
    current_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(current_dir, "Indirilen_Dosyalar")
    
    # 1. Ayarlar (Options) Kısmı - Dosya İndirme (Download) için
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Tarayıcıyı bu ayarlarla başlatalım
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        # ---- BÖLÜM 1: DOSYA YÜKLEME (UPLOAD) ----
        print("\n--- BÖLÜM 1: DOSYA YÜKLEME ---")
        url_upload = "https://the-internet.herokuapp.com/upload"
        driver.get(url_upload)
        
        # Test amaçlı yüklemek için geçici bir .txt dosyası oluşturalım (Aynı dizinde)
        test_file_path = os.path.join(current_dir, "test_upload_verisi.txt")
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write("Bu dosya Selenium öğrenimi için yapay zeka tarafından yaratıldı!")
            
        print(f"📦 Yüklenecek test dosyası oluşturuldu: {test_file_path}")
        
        # Yükleme (Dosya Seç) elementini bul (<input type="file"> etiketine sahip olan)
        upload_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
        
        # Tıklamadan direkt dosya yolunu gönder!
        print("📤 Dosya yolu HTML input'una gönderiliyor...")
        upload_input.send_keys(test_file_path)
        time.sleep(2) # Dosya isminin oraya geldiğini gözlemlemek için bekleyelim
        
        # Submit (Onay) butonuna tıkla
        submit_btn = driver.find_element(By.ID, "file-submit")
        submit_btn.click()
        
        time.sleep(2)
        
        # Yüklemenin başarılı olup olmadığını sayfadaki başlıktan kontrol et
        success_msg = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
        print(f"✅ Yükleme Sonucu: {success_msg}")
        
        
        # ---- BÖLÜM 2: DOSYA İNDİRME (DOWNLOAD) ----
        print("\n--- BÖLÜM 2: DOSYA İNDİRME ---")
        url_download = "https://the-internet.herokuapp.com/download"
        driver.get(url_download)
        
        # Sayfada indirebileceğimiz yüzlerce link var. İlk sıradaki linki bulalım.
        # href özelliği 'download' dizinini içeren bir a etiketi bulacağız:
        first_download_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".example a")))
        indirme_adi = first_download_link.text
        
        print(f"📥 Sayfadaki '{indirme_adi}' adlı dosyaya tıklanıp indiriliyor...")
        # Özel bir klasör rotamız olduğu için (Indirilen_Dosyalar) Chrome bunu Downloads'a değil, 
        # kodumuzun yanındaki 'Indirilen_Dosyalar' adlı dosyaya indirecektir!
        first_download_link.click()
        
        # İndirmenin bitmesi için biraz cömert bekleyelim
        time.sleep(5)
        
        print(f"🎯 Kontrol ediniz: Masaüstünüzde veya proje klasörünüzde 'Indirilen_Dosyalar' adlı yeni bir klasör ve içinde '{indirme_adi}' olmalıdır.")

    except Exception as e:
        print(f"❌ Hata: {e}")
        
    finally:
        print("\n🧹 Tarayıcı tamamen kapatılıyor...")
        driver.quit()
        
        # Yükleme için oluşturduğumuz çöp test dosyasını da bilgisayardan silelim
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

if __name__ == "__main__":
    file_upload_download_practice()
