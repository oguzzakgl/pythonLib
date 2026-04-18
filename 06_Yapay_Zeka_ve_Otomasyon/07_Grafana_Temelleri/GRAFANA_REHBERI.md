# Grafana Nedir? Neden Çok Havalıdır?

Grafana'yı sadece adından duymuş olabilirsiniz ancak dünya çapındaki en büyük şirketlerin **"Veri İzleme ve Dashboard (Kontrol Paneli) Merkezi"** dir.

Diyelim ki Selenium ile harika veriler çektik (Örneğin: Altının günlük alış-satış fiyatları veya sitedeki takipçilerinizin artışı). Biz python'da print yapsak da bu veriler siyah terminal ekranında (console) sayılar olarak kayıp gider. İnsan gözü (özellikle partonlar ve İK uzmanları) sayıları değil, **renkli, canlı, artıp azalan şık pencereleri (grafikleri)** sever!

**İşte Grafana bu noktada devreye girer!**

Grafana, veritabanımıza (SQLite, PostgreSQL vb.) bir hortum bağlar. O veritabanındaki sayıları alır ve bize saniyeler içinde karanlık temalı (Dark Mode), hacker filmlerinden fırlamış gibi duran muazzam Dashboard'lar (Gösterge Panelleri) çizer.

## Grafana'nın Temel Çalışma Mantığı

Çok basit 3 aşaması vardır:

1. **DataSource (Veri Kaynağı):** Grafana'ya "Veriyi Nereden Alacağını" söyleriz. (Bizim projemizde bu, Python ile oluşturacağımız "finance_db.sqlite" veritabanı olacak).
2. **Dashboard (Panel):** Bilgilerin görüneceği ana sayfadır. Portfolyo sitenizdeki ana vitrin gibi düşünün.
3. **Panel (Grafik Kutusu):** Dashboard içindeki her bir kare kutudur. Çizgi grafik (Time series), Çubuk grafik (Bar chart) veya büyük puntolu anlık sayılar (Stat) eklenebilir.

> **Özetle:** Selenium sitelerden veriyi toplar + Pandas bu veriyi temizler + Python bunu SQLite Veritabanına kaydeder -> **Grafana ise bu veritabanına bağlanıp tüm bu süreci harika görselleştirir!**

---

## 💻 Adım Adım Windows İçin Grafana Kurulumu

Grafana yazılım dili veya kütüphane değil, arka planda (Localhost:3000) sürekli çalışan ayrı bir uygulamadır (Server). Bu yüzden bilgisayarımıza bir defa kurmamız gerekiyor.

**1. İndirme:**
- [Grafana Windows İndirme Sayfası](https://grafana.com/grafana/download?platform=windows)'na gidin.
- (Eğer link açılmazsa Google'a `Grafana Download Windows OS` yazabilirsiniz).
- Veya direkt şu linkten Windows Yükleyiciyi (`.msi` uzantılı) indirin: (Şu anki güncel sürümü indirebilirsiniz)

**2. Kurulum İşlemi:**
- İndirdiğiniz `grafana-enterprise-XX.XX.X.windows-amd64.msi` dosyasına çift tıklayın.
- Sürekli "Next" (İleri) diyerek standart her program gibi bilgisayarınıza yükleyin. Özel bir ayar yapmanıza gerek yoktur.
- Kurulum bitince arka planda Grafana Server otomatik olarak çalışmaya başlayacaktır!

**3. İlk Giriş (Localhost):**
- Kurulum bittikten sonra internet tarayıcınızı (Chrome vb.) açın.
- Adres çubuğuna şunu yazın ve Enter'a basın: **`http://localhost:3000`**
- Karşınıza Grafana giriş ekranı gelecek.
- İlk varsayılan şifre ve kullanıcı adı:
  - **Kullanıcı adı:** `admin`
  - **Şifre:** `admin`
- Girdikten sonra sizden kendi yeni güçlü şifrenizi belirlemenizi isteyecektir (İsterseniz *Skip* diyerek geçebilirsiniz ama aklınızda tutacağınız bir şifre girin).

Eğer ekranda Grafana'nın güzel ana ekranını görüyorsanız, sistemimiz veri botlarının şahı olmaya hazır demektir! 🎉
