# FastAPI Nedir, Nerede ve Nasıl Kullanılır?

## 🚀 FastAPI Nedir?
FastAPI, Python ile API (Application Programming Interface) geliştirmek için kullanılan, **modern**, **hızlı** (yüksek performanslı) ve **web framework**'üdür.

Basitçe: **"Benim Python kodum ile İnternet/Mobil Uygulama konuşsun"** dediğin noktada FastAPI devreye girer.

### Neden Çok Popüler?
1.  **Hız:** NodeJS ve Go ile yarışacak kadar hızlıdır (Starlette ve Pydantic sayesinde).
2.  **Otomatik Dokümantasyon:** Kodunu yazarsın, o sana **Swagger UI** (`/docs`) denilen süper bir test ekranını otomatik üretir.
3.  **Kolaylık:** Veri doğrulama (Pydantic) içinde gömülüdür. "Bu veri sayı mı, yazı mı?" diye if-else yazmazsın.
4.  **Asenkron (Async):** `async/await` desteği ile aynı anda binlerce isteği bekletmeden yönetebilir.

---

## 🌍 Nerede Kullanılır?
*   **Mobil Uygulama Backend'i:** Flutter, React Native gibi uygulamalara veri göndermek için.
*   **Web Sitesi Backend'i:** React, Vue, Next.js gibi frontend'lere veri sağlamak için.
*   **Yapay Zeka Modellerini Sunma:** Eğittiğin bir AI modelini (TensorFlow, PyTorch) insanlara açmak için en popüler araçtır.
*   **Mikroservisler:** Büyük sistemleri küçük parçalara bölüp haberleştirmek için.

---

## 🛠️ Nasıl Kullanılır? (Çalışma Mantığı)

FastAPI tek başına çalışmaz, bir **sunucuya (ASGI Server)** ihtiyaç duyar. En popüler sunucu **Uvicorn**'dur.

1.  **Kodunu Yaz:** `app = FastAPI()` diyerek başlarsın.
2.  **Yolu Belirle:** `@app.get("/urunler")` gibi adresler tanımlarsın.
3.  **Çalıştır:** `uvicorn dosya_adi:app --reload` diyerek sunucuyu başlatırsın.

### Örnek Akış:
1.  Sen kodu çalıştırırsın (Uvicorn sunucusu açılır).
2.  Kullanıcı tarayıcıdan `http://localhost:8000/` adresine gider.
3.  Uvicorn bu isteği kapar, FastAPI'ye verir.
4.  FastAPI senin yazdığın fonksiyona (`def ana_sayfa`) gider.
5.  Fonksiyon bir sözlük (`dict`) döndürür.
6.  FastAPI bunu otomatik **JSON**'a çevirip kullanıcıya yollar.

---

## ⚡ Flask ve Django'dan Farkı Ne?
*   **Flask:** Çok esnek ama veri doğrulama (Pydantic) ve asenkron (async) yapısı FastAPI kadar gömülü gelmez.
*   **Django:** Çok büyük ve her şeyi içinde barındırır (Admin paneli vs.) ama öğrenmesi zordur ve FastAPI'ye göre hantaldır.
*   **FastAPI:** İkisinin ortasıdır. Flask kadar basit, Django kadar yetenekli, hepsinden hızlıdır.

---

## 🔍 Swagger UI Nedir? (`/docs`)
FastAPI'nin en sevilen özelliğidir.
*   **Ne İşe Yarar?** Kodunuzdaki tüm fonksiyonları okur ve interaktif bir web sayfası oluşturur.
*   **Neden Kullanılır?** Postman gibi harici programlara gerek kalmadan, doğrudan tarayıcıdan API'nizi test edebilirsiniz.
*   **Nasıl Çalışır?** Tarayıcıda adresin sonuna `/docs` eklemeniz yeterlidir.
    *   **Mavi Butonlar (GET):** Veri çekme istekleri.
    *   **Yeşil Butonlar (POST):** Veri gönderme istekleri.
    *   **Try it out:** Bu butona basarak parametre girip "Execute" diyebilirsiniz.

## 🌐 URL (Endpoint) Mantığı
Adres çubuğundaki o yazılar (`http://127.0.0.1:8000/urunler/5`) aslında birer komuttur.

1.  **Domain (Ev Adresi):** `127.0.0.1` (veya `localhost`) -> "Bu bilgisayar" demek.
2.  **Port (Kapı Numarası):** `:8000` -> Uygulamamızın dinlediği kapı.
3.  **Path (Oda):** `/urunler/{id}` -> Hangi fonksiyonun çalışacağını belirleyen yol.
    *   Sen `/urunler/5` dediğinde, FastAPI hemen koduna bakar:
    *   `@app.get("/urunler/{urun_id}")` satırını bulur.
    *   `urun_id` değişkenine `5` yazar ve fonksiyonu çalıştırır.

## ❓ Swagger UI Sadece Test İçin Mi?
**Hem Evet, Hem Hayır.**

1.  **Geliştirme Aşamasında (Bizim şu an yaptığımız):** Kesinlikle **TEST** içindir. Kodunu yazarsın, Swagger'dan çalışıyor mu diye bakarsın.
2.  **Takım Çalışmasında:** **İLETİŞİM** aracıdır. Frontend (Arayüz) yazan arkadaşına "Al bu linke bak, hangi veriyi göndermen gerektiği orada yazıyor" dersin.
3.  **Gerçek Hayatta (Production):** Genellikle **KAPATILIR** veya şifre ile korunur. Çünkü kötü niyetli kişiler API yapınızı görüp saldırı yapabilir.
    *   Ancak **Halka Açık API** yapıyorsanız (örn: Hava durumu servisi), o zaman açık bırakılır ki insanlar nasıl kullanacağını öğrensin.

