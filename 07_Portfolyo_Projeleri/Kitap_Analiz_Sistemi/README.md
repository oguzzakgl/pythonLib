# 📚 Kitap Analiz ve AI Tahmin Pipeline

Bu proje, bir e-ticaret sitesinden (Books to Scrape) veri toplayan, bu verileri temizleyip analiz eden ve makine öğrenmesi kullanarak kitap reytinglerini tahmin eden uçtan uca bir veri işleme hattıdır.

## 🛠️ Kullanılan Teknolojiler
- **Python:** Ana programlama dili.
- **Selenium:** Web Scraping ve tarayıcı otomasyonu.
- **Pandas:** Veri temizleme ve manipülasyonu.
- **Scikit-Learn:** Makine öğrenmesi (Random Forest).
- **Streamlit:** Interaktif web arayüzü ve dashboard.
- **Joblib:** AI modelinin kaydedilmesi ve yüklenmesi.

## 📂 Proje Yapısı
```text
├── data/
│   ├── raw_books_data.csv       # Botun çektiği ham veriler
│   └── cleaned_books_data.csv   # Temizlenmiş ve ML'e hazır veriler
├── models/
│   └── book_rating_model.joblib # Eğitilmiş Yapay Zeka modeli
├── scraper.py                   # Çok sayfalı Selenium botu
├── analysis.py                  # Veri temizleme ve özellik mühendisliği
├── model_training.py            # AI model eğitimi ve performans testi
└── app.py                       # Streamlit web arayüzü
```

## 🚀 Çalıştırma Adımları

1. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install pandas selenium scikit-learn joblib streamlit matplotlib seaborn
   ```

2. **Web Arayüzünü Başlatın:**
   Eğer veriler ve model zaten mevcutsa doğrudan arayüzü açabilirsiniz:
   ```bash
   streamlit run app.py
   ```

3. **Veriyi Güncellemek ve Modeli Yeniden Eğitmek (Opsiyonel):**
   ```bash
   python scraper.py        # Yeni veri çek
   python analysis.py       # Veriyi temizle
   python model_training.py # Modeli eğit
   ```

## 🚀 Yeni Eklenen Pro Özellikler ✨
- **Dinamik Veri Filtreleme:** Fiyat aralığı ve minimum puan bazlı canlı süzme.
- **Dışa Aktarma:** Filtrelenmiş listeyi tek tıkla **CSV** olarak indirme.
- **Çoklu AI Modeli:** Random Forest ve Linear Regression modelleri arasında seçim yapabilme.
- **Performans Takibi:** Modellerin hata paylarını (MAE) karşılaştırmalı izleme.
- **Scraper:** Web sitesindeki tüm sayfaları gezer ve her kitabın ismini, fiyatını ve reytingini toplar.
- **Analiz:** Fiyat birimlerini temizler, metin tabanlı reytingleri sayısal (1-5) hale getirir.
- **Yapay Zeka:** Kitap isminin uzunluğu ve fiyat bilgisi ile reyting arasındaki ilişkiyi öğrenir.
- **Dashboard:** Kullanıcının girdiği kitap bilgilerine göre AI'nın ne kadar reyting vereceğini tahmin eder.

---
*Bu proje, 'Python Learning Journey' kapsamında veri bilimi ve otomasyon becerilerini birleştirmek amacıyla geliştirilmiştir.*
