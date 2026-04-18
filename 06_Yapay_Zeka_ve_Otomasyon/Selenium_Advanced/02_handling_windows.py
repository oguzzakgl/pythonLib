from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def handling_windows_practice():
    print("🚀 Tarayıcı başlatılıyor...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    try:
        # 1. Ana sayfaya gidelim (Bu site, yeni sekmeler açmayı test etmek için harikadır)
        url = "https://the-internet.herokuapp.com/windows"
        print(f"🌐 {url} adresine gidiliyor...")
        driver.get(url)
        
        # 2. Ana pencerenin kimliğini (ID) kaydedelim
        # Bu ID'yi dönüş biletine benzetebilirsiniz. İşimiz bitince eve (ana sekmeye) dönmek için lazım olacak.
        ana_sayfa_id = driver.current_window_handle
        print(f"🏠 Ana Sayfa ID'si kaydedildi: {ana_sayfa_id}")
        
        # Yeni bir pencere/sekme açacak olan butona tıklayalım
        print("👆 'Click Here' butonuna tıklanıyor...")
        click_here_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
        click_here_link.click()
        
        time.sleep(2) # Yeni sekmenin açıldığını net görebilmek için kısa bir bekleme
        
        # 3. Şu anda açık olan tüm pencerelerin kimliklerini (ID) alalım
        tum_sayfalar = driver.window_handles
        print(f"📚 Şu an açık olan sekme sayısı: {len(tum_sayfalar)}")
        
        # 4. Yeni açılan sekmeye geçiş yapalım
        # tum_sayfalar = [ana_sayfa_id, yeni_sekme_id] şeklinde bir listedir.
        for sekme_id in tum_sayfalar:
            if sekme_id != ana_sayfa_id: # Eğer bu ID, Ana Sayfa ID'miz değilse, demek ki yeni sekmeyiz!
                print("🔄 Kontrol yeni sekmeye geçiriliyor...")
                driver.switch_to.window(sekme_id)
                break
                
        # 5. Artık yeni sekmedeyiz! Burada istediğimiz işlemleri yapabiliriz.
        yeni_sekme_basligi = driver.title
        yeni_sekme_metni = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
        print(f"✨ Yeni sekmenin başlığı: {yeni_sekme_basligi}")
        print(f"✨ Yeni sekmedeki yazı: {yeni_sekme_metni}")
        
        time.sleep(3) # Yeni sayfayı izleyelim
        
        # 6. Yeni sekmedeki işimiz bitti, bu sekmeyi kapatalım (TARAYICIYI DEĞİL)
        print("❌ Yeni sekme kapatılıyor (driver.close)...")
        driver.close() 
        
        time.sleep(2)
        
        # 7. Eve (Ana Sekmeye) Geri Dönüş
        # ÖNEMLİ: Yeni sekmeyi kapatsak bile Selenium eski sekmeye OTOMATİK DÖNMEZ! Bizim geçirmemiz lazım.
        print("🔄 Kontrol tekrar Ana Sekmeye geçiriliyor...")
        driver.switch_to.window(ana_sayfa_id)
        
        # Ana sayfada olduğumuzu doğrulamak için baştaki 'Click Here' yazısını tekrar okuyalım
        # Ana sayfaya döndükten sonra tekrar element etkileşimi yapmak mümkün oldu!
        tekrar_kontrol = driver.find_element(By.LINK_TEXT, "Click Here").text
        print(f"✅ Ana sekmeye başarıyla dönüldü! Görünen buton metni: {tekrar_kontrol}")
        
        time.sleep(3)

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        
    finally:
        # Son olarak driver.quit() kullanarak tüm sekmeleri ve tarayıcıyı temelli kapatıyoruz.
        print("🧹 Tarayıcı tamamen kapatılıyor (driver.quit)...")
        driver.quit()

if __name__ == "__main__":
    handling_windows_practice()

# ÖZET:
# - Yeni sekme açıldıktan sonra etkileşime geçmek için: driver.switch_to.window(yeni_id) kullanılır.
# - Sadece mevcut sekmeyi kapatmak için driver.close() kullanılır.
# - Tamamen kapatmak ve Selenium'u bitirmek için driver.quit() kullanılır.
