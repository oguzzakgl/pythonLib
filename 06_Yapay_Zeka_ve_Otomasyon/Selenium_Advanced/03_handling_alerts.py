from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def handling_alerts_practice():
    print("🚀 Tarayıcı başlatılıyor...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Alerts örneklerinin olduğu harika bir test sitesine gidelim
        url = "https://the-internet.herokuapp.com/javascript_alerts"
        print(f"🌐 {url} adresine gidiliyor...")
        driver.get(url)
        
        # Sonucu görmek için sitenin alt kısmında "Result" yazan bir alan var, oradan sonuçları okuyacağız
        sonuc_metni = driver.find_element(By.ID, "result")

        # --- TÜR 1: Normal Alert (Sadece 'Tamam' denilen bilgi mesajı) ---
        print("\n1️⃣ Tür 1: Normal Alert (Bilgi Uyarı) testi yapılıyor...")
        normal_alert_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
        normal_alert_btn.click()
        time.sleep(1) # Animasyon için kısa bekleme

        secilen_alert = wait.until(EC.alert_is_present()) # Alertin çıkmasını bekle ve al
        print(f"   💬 Alert üzerindeki yazı: {secilen_alert.text}")
        secilen_alert.accept() # 'Tamam'a tıklayarak Alerti kabul et!
        print(f"   ✅ Site sonucu: {sonuc_metni.text}")
        time.sleep(2)


        # --- TÜR 2: Confirm Alert (Onay Uyarıları - Tamam/İptal) ---
        print("\n2️⃣ Tür 2: Confirm Alert (Onay Uyarı) testi yapılıyor...")
        confirm_alert_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
        
        # İlk deneme: İptal Et (Dismiss)
        confirm_alert_btn.click()
        time.sleep(1)
        iptal_alert = wait.until(EC.alert_is_present())
        print("   ❌ Alerte 'İptal / Cancel' deniliyor...")
        iptal_alert.dismiss() # 'İptal'e tıkla!
        print(f"   ✅ Site sonucu: {sonuc_metni.text}")
        time.sleep(2)
        
        # İkinci deneme: Kabul Et (Accept)
        confirm_alert_btn.click()
        time.sleep(1)
        kabul_alert = wait.until(EC.alert_is_present())
        print("   ✔️ Alerte 'Tamam / OK' deniliyor...")
        kabul_alert.accept() # 'Tamam'a tıkla!
        print(f"   ✅ Site sonucu: {sonuc_metni.text}")
        time.sleep(2)


        # --- TÜR 3: Prompt Alert (Girdi Bekleyen Uyarılar) ---
        print("\n3️⃣ Tür 3: Prompt Alert (Metin Girişi Bekleyen Uyarı) testi yapılıyor...")
        prompt_alert_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
        prompt_alert_btn.click()
        time.sleep(1)
        
        giris_alert = wait.until(EC.alert_is_present())
        gonderilecek_metin = "Selenium Harika!"
        
        print(f"   ⌨️ Alerte şu metin gönderiliyor: '{gonderilecek_metin}'")
        giris_alert.send_keys(gonderilecek_metin) # Alerte yazımızı yolladık
        time.sleep(1) # Yazdığımızı görmek için bekleyelim
        giris_alert.accept() # Göndermek için Onayladık
        
        print(f"   ✅ Site sonucu: {sonuc_metni.text}")
        time.sleep(3)


    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        
    finally:
        print("\n🧹 Tarayıcı tamamen kapatılıyor...")
        driver.quit()

if __name__ == "__main__":
    handling_alerts_practice()

# ÖZET:
# - HTML olmayan pop-up pencereler için: element = driver.switch_to.alert kullanılır.
# - Çıkmasını güvenle beklemek için alert_is_present() condition'u tavsiye edilir.
# - Dört temel metot vardır: accept(), dismiss(), text ve send_keys("yazı").
