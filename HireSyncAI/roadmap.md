# 🚀 HireSync AI - Proje Yol Haritası (Roadmap)

Bu dosya, HireSync AI projesinin gelişim adımlarını ve mülakat öncesi hazırlık planını içerir.

---

## ✅ 1. Aşama: Planlama ve Altyapı (Tamamlandı)
- [x] **Proje Vizyonu:** Hirethink şirketinin HR odaklı yapısına uygun CV analiz sistemi tasarlandı.
- [x] **Teknoloji Seçimi:** FastAPI (Backend), spaCy & Scikit-learn (AI), Modern Vanilla JS (Frontend) kararlaştırıldı.
- [x] **Klasör Yapısı:** Uygulamanın temel iskeleti (MVC benzeri yapı) kuruldu.
- [x] **Kütüphanelerin Kurulumu:** Gerekli tüm Python kütüphaneleri yüklendi.

## 🎨 2. Aşama: Frontend & Tasarım (Tamamlandı)
- [x] **Modern UI Kurulumu:** Tam siyah ve bordo (kırmızı) temalı, profesyonel bir Dashboard tasarlandı.
- [x] **Responsive Tasarım:** Ekranın her boyutunda (Mobil/Desktop) kaydırma yapmadan çalışacak şekilde optimize edildi.
- [x] **Dinamik Grafikler:** Uyumluluk skoru için asimetrik ve modern bir yarım ay (speedometer) grafiği eklendi.
- [x] **UX İyileştirmeleri:** Sürükle-bırak dosya yükleme ve interaktif butonlar eklendi.

## 🛠️ Kodlama Sırası ve Dosya Görevleri

Projenin canlanması için şu sırayla dosyaları dolduracağız:

### 1️⃣ `app/engine.py` (Projenin Beyni)
*Önce burayı yazmalıyız çünkü API ve Frontend buradaki fonksiyonlara muhtaç.*
- [ ] `extract_text_from_any(file)`: PDF ve Word okuma mantığı.
- [ ] `get_skills(text)`: spaCy ile metinden yetenekleri ayıklama.
- [ ] `match_job_description(cv, jd)`: Skikit-learn ile uyumluluk puanı hesaplama.

### 2️⃣ `app/main.py` (Sistemin Kapısı)
*Beyin (Engine) hazır olduktan sonra dış dünyaya açılan kapıyı kuracağız.*
- [ ] FastAPI sunucusunu ayağa kaldırma.
- [ ] `/upload` endpoint'i ile dosya kabul etme.
- [ ] Gelen dosyayı `engine.py`'ye gönderip sonuçları JSON olarak döndürme.

### 3️⃣ `ui/script.js` (Gerçek Bağlantı)
*Tasarım hazır, şimdi onu gerçek veriye bağlayacağız.*
- [ ] `fetch()` ile FastAPI sunucusuna istek atma.
- [ ] Simülasyon kodlarını silip gerçek analiz sonuçlarını ekrana basma.

### 4️⃣ `Dockerfile` & `README.md` (Final Dokunuş)
- [ ] Tüm projeyi tek tuşla çalışır hale getirme.
- [ ] Mülakat için etkileyici sunum metni.

---
**Not:** Kod yazmaya her zaman içten dışa (Logic -> API -> UI) doğru ilerlemek en sağlıklı yoldur.
