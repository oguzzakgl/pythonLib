# SELENIUM ADVANCED (İLERİ SEVİYE) REHBERİ

Bu döküman, Selenium'un ileri seviye özelliklerini tek bir yerde toplayan başvuru kaynağıdır.

---

## BÖLÜM 1: ⚙️ Tarayıcı Ayarları ve Headless Mode

Gerçek projelerde tarayıcıyı her seferinde manuel açmak yavaş ve gereksiz olabilir. `ChromeOptions` kullanarak tarayıcının davranışlarını kontrol edebiliriz.

### 1. Headless Mode (Görünmez Tarayıcı)
Tarayıcıyı bir arayüz olmadan arka planda çalıştırır. Sunucularda (Server) çalışırken zorunludur.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # Tarayıcıyı gösterme
options.add_argument("--disable-gpu") # Performans artışı

driver = webdriver.Chrome(options=options)
```

### 2. Sık Kullanılan Diğer Ayarlar

| Komut | Açıklama |
| :--- | :--- |
| `--start-maximized` | Tarayıcıyı tam ekranda başlatır. |
| `--window-size=1920,1080` | Belirli bir pencere boyutu ayarlar. |
| `--incognito` | Gizli sekmede açar. |
| `--disable-notifications` | Bildirim izinlerini engeller. |
| `user-agent=...` | Tarayıcı kimliğini değiştirir. |

### 3. Performans İpuçları: Resimleri Engelleme
Web scraping sırasında resimlerin yüklenmesini engellemek hızı %50'den fazla artırabilir.

```python
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
```

> [!TIP]
> Headless modda çalışırken bazen siteler bot olduğunuzu daha kolay anlar. Bunu engellemek için her zaman bir **User-Agent** tanımlamak iyi bir pratiktir.

---

## BÖLÜM 2: 📑 Sekmeler (Tabs) ve Pencereler (Windows) Arası Geçiş

Web sitelerinde gezinirken bazen bir butona tıkladığımızda veya bir linke dokunduğumuzda yeni bir **Sekme (Tab)** veya tamamen farklı bir tarayıcı **Penceresi (Window)** açılır. 

Böyle bir durumda Selenium, siz aksini söyleyene kadar eski (ilk açtığı) sayfada kalmaya devam eder. Yani yeni açılan sekmedeki bir butona tıklamak isterseniz **ElementBulunamadı (NoSuchElementException)** hatası alırsınız. Çünkü Selenium'un "odak noktası" (focus) hala ilk sayfadadır.

### 1. Window Handle (Pencere Kimliği) Nedir?
Selenium açtığı her bir sekmeye ve pencereye benzersiz bir kimlik (ID) atar. Tıpkı her insanın farklı bir T.C. Kimlik Numarası olması gibi. Biz sekmeler arasında gezinmek için bu kimlik numaralarını kullanırız.

### 2. Önemli Komutlar:

- `driver.current_window_handle`: Selenium'un şu anda aktif olarak bulunduğu (odaklandığı) sekmenin **kimliğini**(ID) verir.
- `driver.window_handles`: Tarayıcıda açık olan **tüm** sekmelerin kimliklerini bir liste (list) halinde döndürür. Örneğin: `[ID_1, ID_2]`. Listenin ilk elemanı (`[0]`) ilk sekme, ikinci elemanı (`[1]`) ikinci sekme demektir.
- `driver.switch_to.window(Pencere_ID)`: Selenium'un odağını (kontrolünü), ID'sini belirttiğimiz yeni sekmeye geçirir.
- `driver.close()`: Sadece şu anda içinde bulunduğumuz aktif **sekmeyi kapatır**, ancak tarayıcıyı tamamen kapatmaz (eğer başka sekmeler açıksa).
- `driver.quit()`: Açık olan **tüm sekmeleri ve tarayıcıyı** kökünden kapatır.

### Mantık Şeması - Sekme Değiştirme Nasıl Yapılır?

1. Şu anki ana pencerenin ID'sini kaydet:
   `ana_sayfa = driver.current_window_handle`
2. Yeni sekme açacak olana butona/linke tıkla.
3. Açık olan tüm pencerelerin listesini al:
   `tum_sayfalar = driver.window_handles`
4. Döngü ile (veya direkt `tum_sayfalar[1]` diyerek) yeni sekmeyi bul ve geçiş yap:
   `driver.switch_to.window(yeni_sayfa_id)`
5. Yeni sekmedeki işini bitirince sekmeyi kapat:
   `driver.close()`
6. Ana sekmeye geri dön:
   `driver.switch_to.window(ana_sayfa)`

---

## BÖLÜM 3: ⚠️ Uyarı Pencereleri (Alerts) Yönetimi

Web sitelerinde gezinirken sık sık JavaScript ile oluşturulmuş, genelde ekranın en üst kısmından beliren küçük uyarı pencereleri (Alerts) ile karşılaşırız. 

Bu pencereler HTML sayfasının bir parçası **değildir**. Bu nedenle pencerelere sağ tıklayıp "İncele" (Inspect) diyerek elementlerinin ID'sini veya Class'ını **bulamayız**. Selenium bu pencerelerle etkileşime girmek için özel yöntemler sunar.

### 1. Alert (Uyarı) Türleri Nelerdir?

1. **Normal Alert (Bilgi Uyarıları):** Sadece "Tamam" (OK) diyerek kapatabildiğimiz sade bilgi mesajlarıdır.
2. **Confirm Alert (Onay Uyarıları):** Bize "Emin misiniz?" diye soran ve "Tamam" (OK) veya "İptal" (Cancel) diyebildiğimiz uyarılardır.
3. **Prompt Alert (Girdi Uyarıları):** Bize bir soru sorup içine **metin girmemizi** isteyen uyarılardır.

### 2. Önemli Komutlar:

Tüm bu uyarı pencerelerini yönetmek için öncelikle Selenium'un odağını açık olan uyarının üzerine geçirmeliyiz:
`alert_penceresi = driver.switch_to.alert`

Bu geçişi yaptıktan sonra kullanabileceğimiz 4 ana komut vardır:

- `alert_penceresi.accept()`: "Tamam" / "OK" / "Evet" butonuna tıklar. (Kabul eder)
- `alert_penceresi.dismiss()`: "İptal" / "Cancel" / "Hayır" butonuna tıklar. (Reddeder)
- `alert_penceresi.text`: Uyarının bize gösterdiği yazıyı (mesajı) okuyup alır.
- `alert_penceresi.send_keys("Yazılacak Metin")`: Prompt (Girdi) türündeki uyarılara klavyeden metin gönderir.

### Mantık Şeması - Alert Yönetimi Nasıl Yapılır?

1. Uyarı penceresini tetikleyecek web elementini bul ve tıkla: `driver.find_element(By.ID, "uyari-butonu").click()`
2. (Opsiyonel) Uyarının çıkmasını bekle: `WebDriverWait(driver, 5).until(EC.alert_is_present())`
3. Odağı sayfadan (HTML) uyarı penceresine (Alert) geçir: `gelen_uyari = driver.switch_to.alert`
4. Gereken işlemi yap: `gelen_uyari.accept()`
5. Uyarı kapandıktan sonra Selenium'un **odağı otomatik olarak HTML sayfaya geri döner**.

---

## BÖLÜM 4: 🖼️ iFrame (Sayfa İçinde Sayfa) Yönetimi

Bazen bir web sayfasını açtığımızda, o sayfanın içinde gömülü olarak duran başka bir web sayfası (Örneğin: YouTube videosu, Google haritası veya bir ödeme formu) bulunur. Bu HTML içine gömülü bağımsız sayfalara **`<iframe>`** (Inline Frame) denir.

Selenium ile sayfa içindeki bir butona tıklamak istediğimizde, eğer o buton bir iFrame'in **içindeyse**, Selenium o butonu **BULAMAZ**. Selenium sadece en dıştaki ana HTML dökümanını (Default Content) görür, iFrame'in içine otomatik bakmaz.

### 1. iFrame'in İçine Girmek
Kasanın içine üç farklı şekilde girebiliriz:
- `driver.switch_to.frame(0)` (Sayfadaki ilk iFrame'e indeks no ile girmek)
- `driver.switch_to.frame("iframe_id_veya_name")` (Adıyla girmek)
- **(En Güvenlisi)** Önce iFrame elementini bulup sonra içine girmek:
  ```python
  benim_katmanim = driver.find_element(By.ID, "dış_kod")
  driver.switch_to.frame(benim_katmanim)
  ```

### 2. Tekrar Ana Sayfaya Geri Dönmek (Çıkış)
İçerideki işimiz bitti. Kasadan çıkıp tekrar odadaki diğer eşyalarla ilgilenmek istiyorsak:
- `driver.switch_to.default_content()`: Bizi doğrudan en dıştaki ana sayfaya geri fırlatır.

### Mantık Şeması
1. Sayfaya git.
2. Selenium'un odağını iFrame'e geçir: `driver.switch_to.frame("video_kutu")`
3. İçerideki işlemi yap: `driver.find_element(By.ID, "play_button").click()`
4. İşin bitince ana sayfaya dön: `driver.switch_to.default_content()`

---

## BÖLÜM 5: 📜 JavaScript Komutları Çalıştırma (Execute Script)

Bazen **web sitesindeki elementler Selenium'dan saklanmak ister.** 
Örneğin üzerine başka görünmez bir katman binen butonlara tıklayamazsınız veya sayfayı aşağı kaydırmadan bazı elementler yüklenmez.

İşte tam bu anlarda Selenium'un "Süper Gücünü" devreye sokarız: **Tarayıcının içine doğrudan saf JavaScript kodu enjekte edip o kodu çalıştırmak!** 

### En Sık Kullanılan 3 JavaScript Komutu

Tüm JS komutları `driver.execute_script("JS_KODU_BURAYA")` metodu ile çalıştırılır.

**1. Sayfa Kaydırma (Scroll) İşlemleri**
- Belirli bir piksel kadar aşağı kaydırmak için: `driver.execute_script("window.scrollBy(0, 500);")` 
- Sayfanın EN ALTINA kadar kaydırmak için: `driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")`
- Belirli bir element görünene kadar kaydırmak için:
  ```python
  hedef_buton = driver.find_element(By.ID, "sakli_buton")
  driver.execute_script("arguments[0].scrollIntoView(true);", hedef_buton)
  ```

**2. İnatçı Butonlara Zorla Tıklamak**
```python
inatci_buton = driver.find_element(By.ID, "tiklanmayan_buton")
driver.execute_script("arguments[0].click();", inatci_buton)
```

**3. Değer Döndüren Sorgular Yapmak**
```python
js_baslik = driver.execute_script("return document.title;")
print(js_baslik)
```

---

## BÖLÜM 6: 📤 Dosya Yükleme (Upload) ve 📥 İndirme (Download)

### 1. Dosya Yükleme (File Upload) İşlemi
Bir sitede `Dosya Seç` butonunu gördüğünüzde (HTML kodunda `<input type="file">`), bu butona gerçekte tıklamanıza gerek yoktur. Sadece o kutuya **dosyanın bilgisayarımızdaki TAM YOLUNU** göndermemiz yeterlidir.

```python
# 1. Önce yükleme butonunu (input elementini) bul
yukleme_kutusu = driver.find_element(By.ID, "file-upload")

# 2. Dosya yolunu send_keys ile gönder (Tıklamadan!)
dosya_yolu = "C:\\Users\\Kullanici\\Desktop\\resim.png"
yukleme_kutusu.send_keys(dosya_yolu)

# 3. Gerekirse onaylama butonuna bas (Sitenin Submit butonuna tıkla)
driver.find_element(By.ID, "file-submit").click()
```

### 2. Dosya İndirme (File Download) İşlemi
Bir dosyayı İndirmek için sadece sitedeki indirme linkine tıklamanız yeterlidir. Ancak açılacak olan uyarı pencerelerini ve indirme yolunu **Options** ile önceden ayarlamalıyız.

```python
from selenium.webdriver.chrome.options import Options

ayarlar = Options()
indirme_yolu = "C:\\Users\\Kullanici\\Desktop\\BenimBotum"

prefs = {
    "download.default_directory": indirme_yolu, 
    "download.prompt_for_download": False,      # Soru sorma! Direkt indir.
    "directory_upgrade": True
}
ayarlar.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=ayarlar)
```
