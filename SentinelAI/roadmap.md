# 🛰️ SentinelAI Gelişim Yol Haritası (Roadmap)

SentinelAI projesini sıfırdan "Senior" seviyesine taşımak için izleyeceğimiz adım adım plan:

## 📍 1. Adım: Proje Altyapısı (Skeleton & Container)
- [ ] **Dockerize Etme:** Uygulamanın her ortamda aynı çalışması için `Dockerfile` ve `docker-compose.yml` dosyalarının hazırlanması.
- [ ] **PostgreSQL Kurulumu:** Verilerin kalıcı olması için veritabanı konteynerinin ayağa kaldırılması.

## 📍 2. Adım: Veri Tasarımı ve Simülasyon (Faker)
- [ ] **Data Generator:** API henüz hazır değilken test yapabilmek için `Faker` ile gerçekçi finansal veri akışı oluşturulması.
- [ ] **Şema Tanımları:** Veritabanı tablolarının (SQLAlchemy) ve API veri modellerinin (Pydantic) tasarlanması.

## 📍 3. Adım: API Geliştirme (FastAPI)
- [ ] **Endpoint Yazımı:** `/predict` ve `/history` uçlarının asenkron olarak kodlanması.
- [ ] **Validasyon:** Hatalı verilerin sisteme girmesini engellemek için Pydantic v2 validatörlerinin eklenmesi.

## 📍 4. Adım: Sahtekarlık Tespit Motoru (Logic & ML)
- [ ] **Kural Bazlı Analiz:** Basit Python mantığı ile (örn: limit aşımı, konum uyuşmazlığı) ilk savunma hattının kurulması.
- [ ] **ML Entegrasyonu:** Scikit-learn kullanarak verilerdeki anomalileri yakalayan yapay zeka modelinin eğitilmesi.

## 📍 5. Adım: Gerçek Dünya Testi (Kaggle)
- [ ] **Big Data Import:** Kaggle'dan indirilen milyonlarca satırlık gerçek kredi kartı fraud verisinin sisteme entegre edilmesi.
- [ ] **Performans Ölçümü:** Yazdığımız modelin gerçek veriler üzerindeki başarı oranının (Precision/Recall) test edilmesi.

## 📍 6. Adım: İleri Seviye (Level 2 & Level 3 Hazırlık)
- [ ] **Caching:** Redis ile sık sorgulanan verilerin hızlandırılması.
- [ ] **Background Tasks:** Celery ile ağır işlemlerin arka planda yapılması.

---
**Önemli:** Her adımdan sonra testler yapılacak ve bir sonraki adıma ancak sistem kararlı olduğunda geçilecektir.
