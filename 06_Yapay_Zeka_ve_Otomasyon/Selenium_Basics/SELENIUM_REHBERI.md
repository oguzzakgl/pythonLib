# 🌐 Selenium Tam Rehber: Temellerden Web Scraping'e

Bu rehber, Selenium kütüphanesini kullanarak web otomasyonu ve veri çekme işlemlerini adım adım öğrenmeniz için hazırlanmıştır.

---

## 1. Selenium'a Giriş: Temeller ve Kurulum

Selenium, web tarayıcılarını otomatize etmek için kullanılan en popüler kütüphanedir. Genellikle **Web Scraping** (Veri Çekme) ve **Test Otomasyonu** için kullanılır.

### 🛠️ Neden Selenium?
- **Dinamik İçerik:** JavaScript ile yüklenen verileri çekebilir.
- **Kullanıcı Etkileşimi:** Butonlara tıklayabilir, formları doldurabilir.
- **Gerçek Tarayıcı Deneyimi:** Chrome, Firefox gibi gerçek tarayıcıları yönetir.

### 📥 Kurulum
1. `pip install selenium`
2. **WebDriver:** Selenium 4.6+ ile artık otomatik yönetiliyor!

### 🚀 İlk Script
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Sayfa Başlığı:", driver.title)
driver.quit()
```

---

## 2. Element Bulma (Locators)

Web sayfalarındaki öğelerle etkileşime girmek için önce onları bulmamız gerekir.

| Yöntem | Kod Örneği | Açıklama |
| :--- | :--- | :--- |
| **ID** | `By.ID, "user-name"` | En hızlı ve en güvenilir yöntem. |
| **Name** | `By.NAME, "password"` | Form elemanları için yaygın. |
| **Class Name** | `By.CLASS_NAME, "btn"` | CSS sınıflarını kullanır. |
| **XPath** | `By.XPATH, "//input"` | Sayfa yapısı üzerinden her şeyi bulabilir. |
| **CSS Selector**| `By.CSS_SELECTOR, ".a"`| Modern ve esnek yöntem. |

### ⌨️ Temel Etkileşimler
- `element.send_keys("Text")`: Yazı yazar.
- `element.click()`: Tıklar.
- `element.clear()`: Metni temizler.

---

## 3. Bekleme Stratejileri (Waits)

Hataları önlemek için elementlerin yüklenmesini beklemeliyiz.

1. **Implicit Wait:** `driver.implicitly_wait(10)` (Tüm öğeler için genel bekleme).
2. **Explicit Wait:** Belirli bir öğe için belirli bir koşulu bekler.
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "id")))
```
> [!IMPORTANT]
> Profesyonel projelerde her zaman **Explicit Wait** tercih edilmelidir. `time.sleep()` kullanımından kaçının.

---

## 4. Sayfa Etkileşimleri: Scroll & Select

### 🖱️ Sayfayı Kaydırma (Scrolling)
JavaScript komutları ile yapılır:
- `driver.execute_script("window.scrollBy(0, 500);")` (500px aşağı).
- `driver.execute_script("arguments[0].scrollIntoView();", element)` (Elemente git).

### 🔽 Açılır Menüler (Select)
```python
from selenium.webdriver.support.ui import Select
dropdown = Select(driver.find_element(By.ID, "drop"))
dropdown.select_by_visible_text("Türkiye")
```

---

## 5. ActionChains: Gelişmiş Fare ve Klavye

Karmaşık hareketler (Hover, Drag&Drop) için kullanılır.

- `move_to_element(el)`: Hover (Üzerine gelme).
- `context_click(el)`: Sağ tık.
- `drag_and_drop(src, tgt)`: Sürükle ve bırak.

```python
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(element).perform() # .perform() UNUTMA!
```

---

## 📊 6. Web Scraping (Veri Çekme) Mantelitesi

1. **Siteye Git:** `driver.get(url)`
2. **Kapsayıcıları Bul:** `driver.find_elements(By.CLASS_NAME, "item")`
3. **Döngüye Al:** Her öğenin içindeki başlık, fiyat vb. bilgilerini ayıkla.
4. **Kaydet:** Pandas kullanarak CSV veya Excel'e dönüştür.

```python
import pandas as pd
df = pd.DataFrame(liste)
df.to_csv("veriler.csv", index=False)
```
