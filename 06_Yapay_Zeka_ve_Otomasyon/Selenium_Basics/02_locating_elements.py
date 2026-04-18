from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
SELENIUM ELEMENT BULMA VE ETKİLEŞİM
----------------------------------
Bu script, bir web sayfasındaki elementleri nasıl bulacağımızı ve
onlarla nasıl etkileşime gireceğimizi (yazma, tıklama vb.) gösterir.
"""

def locating_elements_practice():
    # Tarayıcıyı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Uygulama sitesine gidelim (Örnek: Wikipedia - Arama yapması kolaydır)
        url = "https://www.wikipedia.org/"
        print(f"🌐 {url} adresine gidiliyor...")
        driver.get(url)
        
        # 1. Arama kutusunu ID ile bulalım
        # inspect -> <input id="searchInput" ...>
        search_box = driver.find_element(By.ID, "searchInput")
        print("✅ Arama kutusu ID ile bulundu.")
        
        # 2. Arama kutusuna bir şeyler yazalım
        search_text = "Python (programming language)"
        print(f"✍️ '{search_text}' yazılıyor...")
        search_box.send_keys(search_text)
        
        # Gözlemlemek için kısa bir bekleyiş
        time.sleep(2)
        
        # 3. Enter tuşuna basarak arama yapalım
        print("⌨️ Enter tuşuna basılıyor...")
        search_box.send_keys(Keys.ENTER)
        
        # 4. Yeni sayfada başlığı (title) kontrol edelim
        time.sleep(3) # Sayfanın yüklenmesi için basit bir bekleme
        print(f"📄 Mevcut Sayfa Başlığı: {driver.title}")
        
        # 5. Sayfadaki ilk başlığı Class Name ile bulalım
        # Wikipedia makale başlıkları genellikle 'mw-page-title-main' class'ına sahiptir
        try:
            main_title = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
            print(f"🎯 Makale Başlığı Doğrulandı: {main_title.text}")
        except:
            print("⚠️ Makale başlığı class ile bulunamadı, farklı bir tema olabilir.")

        print("\n🎉 Başarıyla arama yapıldı ve sonuçlar görüntülendi!")
        time.sleep(5)

    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")
    
    finally:
        # Tarayıcıyı kapat
        print("🧹 Tarayıcı kapatılıyor...")
        driver.quit()

# ÖZET: Web sayfalarındaki 'ID', 'Name', 'XPath' gibi adresleri kullanarak 
# elementlere nasıl ulaşacağımızı ve onlarla (tıklama, yazı yazma) nasıl konuşacağımızı öğreniyoruz.

if __name__ == "__main__":
    locating_elements_practice()
