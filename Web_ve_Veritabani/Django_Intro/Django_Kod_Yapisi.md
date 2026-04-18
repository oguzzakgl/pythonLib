# 🏗️ Django Kod Yapısı (Hangi Dosya Ne Yapar?)

Django projelerinde her dosyanın çok net bir görevi vardır. Karışıklık olmaması için bu görevler ayrılmıştır.

## 📂 Ana Dosyalar

### 1. `models.py` (Veri Tabanı Şefi 🗄️)
*   **Görevi:** Verilerin nasıl saklanacağını belirler.
*   **Ne yazarız?** "User tablosunda isim ve şifre olsun", "MarketData tablosunda fiyat ve tarih olsun".
*   *Örnek:*
    ```python
    class KriptoPara(models.Model):
        isim = models.CharField(max_length=50) # Örn: Bitcoin
        fiyat = models.FloatField()            # Örn: 45000.50
    ```

### 2. `views.py` (Mantık İşleri / Kontrolör 🧠)
*   **Görevi:** Sitenin beynidir. Veriyi alır, işler ve sayfaya gönderir.
*   **Ne yazarız?** "Veritabanından Bitcoin fiyatını çek, doları TL'ye çevir ve kullanıcıya göster".
*   *Örnek:*
    ```python
    def ana_sayfa(request):
        bitcoin = KriptoPara.objects.get(isim="Bitcoin")
        return render(request, 'anasayfa.html', {'fiyat': bitcoin.fiyat})
    ```

### 3. `urls.py` (Adres Defteri / Navigasyon 📍)
*   **Görevi:** Hangi linke tıklayınca hangi fonksiyonun çalışacağını söyler.
*   **Ne yazarız?** `site.com/bitcoin` -> `ana_sayfa` fonksiyonunu çalıştır.

### 4. `templates/` (Görünüm / HTML 🎨)
*   **Görevi:** Kullanıcının ekranda gördüğü kutucuklar, renkler, yazılar.
*   **Ne yazarız?** Standart HTML kodları.
*   *Örnek:* `<h1>Bitcoin Fiyatı: {{ fiyat }}</h1>`

### 5. `admin.py` (Yönetim Paneli 🛠️)
*   **Görevi:** Hangi tabloların admin panelinde görüneceğini ayarlar.
*   **Ne yazarız?** `admin.site.register(KriptoPara)` diyerek panelden coin ekleyip silmeyi açarız.

---

## 🔄 Özet Akış
1.  Kullanıcı **/bitcoin** yazar (**urls.py** yakalar).
2.  **views.py** çalışır, **models.py**'dan fiyatı sorar.
3.  Gelen fiyatı **html** dosyasına koyar ve kullanıcıya gönderir.
