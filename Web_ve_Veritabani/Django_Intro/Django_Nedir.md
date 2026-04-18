# 🌍 Django Nedir? (Python'un Süper Gücü)

Django, Python ile yazılmış, dünyanın en popüler ve güçlü **Web Geliştirme Çatısıdır** (Web Framework). 
Instagram, Pinterest, Spotify ve NASA gibi devler, sitelerinin arkasında Django kullanır.

## 🤔 Neden "Çatı" (Framework) Diyoruz?
Bir ev yapacağını düşün. 
*   **Python:** Çimentodur, tuğladır. Tek başına ev yapmak zordur.
*   **Django:** Hazır kolonları, duvarları, çatısı, tesisatı çekilmiş bir evin kaba inşaatıdır. Sen sadece içine girip boyasını, mobilyasını (tasarımını) yaparsın.

Sana "Sıfırdan üyelik sistemi yaz" demez, içinde hazır gelir. "Güvenlik açığını kapat" demez, kendisi kapatır.

---

## 🏗️ Django'nun Çalışma Mantığı (MVT Yapısı)
Django bir restorana benzer. Müşteri (Kullanıcı) gelir ve bir yemek (Sayfa) ister.

### 1. 🔗 URLs (Menü)
Müşteri garsona "Ben `/kripto` sayfasını istiyorum" der.
*   Django'da buna **`urls.py`** bakar. İsteği alır ve doğru aşçıya (View) iletir.

### 2. 👨‍🍳 Views (Aşçı - Beyin)
Aşçı siparişi alır.
*   "Bu müşteri kim? Giriş yapmış mı?" diye bakar.
*   "Hangi malzemeler (Veriler) lazım?" diye düşünür.
*   Gidip kilerciye (Model) "Bana Bitcoin fiyatlarını ver" der.
*   Bu dosyalar **`views.py`** içindedir.

### 3. 📦 Models (Kilerci - Veritabanı)
Kilerci, mutfağın deposudur.
*   Aşçı ne isterse (SQL bilmesine gerek kalmadan) veritabanından onu getirir.
*   "Bitcoin: $45.000" bilgisini aşçıya verir.
*   Bu dosyalar **`models.py`** içindedir.

### 4. 🍽️ Templates (Tabak Sunumu - Tasarım)
Aşçı yemeği pişirdi (Veriyi hazırladı). Ama müşteriye tencereyle götüremez.
*   Güzel bir tabakta (HTML Sayfası) sunması gerekir.
*   Bu HTML dosyaları **`templates/`** klasöründedir.

---

## 🚀 Özetle CoinMind Projesi Nasıl Çalışacak?
1.  Sen tarayıcıya `coinmind.com/bitcoin` yazacaksın (**URLs**).
2.  Django diyecek ki: "Bu kullanıcı Bitcoin sayfasını istiyor, `market` uygulamasındaki aşçıya haber ver" (**Views**).
3.  Aşçı (`views.py`) depodan Bitcoin'in son fiyatını isteyecek (**Models**).
4.  Gelen fiyatı şık bir HTML şablonuna koyup sana geri gönderecek (**Templates**).

Ve Django'nun en güzel yanı: **Admin Paneli**.
Sen kod yazmadan, hazır bir panelden "Yeni Coin Ekle", "Kullanıcı Sil" gibi işlemleri yapabileceksin.
