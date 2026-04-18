from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
SELENIUM ACTIONCHAINS (FARE VE KLAVYE)
-------------------------------------
Bu script, fareyi bir elementin üzerine getirme (hover),
sağ tıklama ve sürükleme gibi gelişmiş eylemleri gösterir.
"""

def action_chains_practice():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    
    try:
        # 🟢 Örnek 1: Mouse Hover (Üzerine Gelme)
        # eBay ana sayfasında "Electronics" menüsünün üzerine gelelim
        print("🌐 eBay açılıyor...")
        driver.get("https://www.ebay.com")
        
        electronics_menu = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Electronics")))
        
        print("🖱️ 'Electronics' menüsünün üzerine geliniyor (Hover)...")
        actions.move_to_element(electronics_menu).perform()
        time.sleep(3) # Alt menünün açıldığını görmek için
        
        # 🟢 Örnek 2: Drag and Drop (Sürükle ve Bırak)
        # Bu işlem için popüler bir test sitesine gidelim
        print("\n🌐 Sürükle-Bırak testi için yeni siteye gidiliyor...")
        driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
        
        source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        target = driver.find_element(By.ID, "droppable")
        
        print("📦 Öğe tutuluyor ve kutuya sürükleniyor...")
        actions.drag_and_drop(source, target).perform()
        
        # Sonucu doğrula
        if "Dropped!" in target.text:
            print("✅ Sürükle-Bırak başarılı!")
        
        time.sleep(3)

        # 🟢 Örnek 3: Context Click (Sağ Tık)
        print("\n🖱️ Hedef elemente sağ tıklanıyor...")
        actions.context_click(target).perform()
        time.sleep(3)

    except Exception as e:
        print(f"❌ Hata: {e}")
    
    finally:
        driver.quit()
        print("\n🧹 Tarayıcı kapatıldı.")

if __name__ == "__main__":
    action_chains_practice()

# ÖZET: Fareyle bir şeyin üzerine gelmek (Hover), sağ tıklamak veya 
# sürükleyip bırakmak gibi daha karmaşık ve insansı hareketleri ActionChains ile yapıyoruz.
