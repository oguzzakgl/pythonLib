# 🗄️ Backend Dünyası: API ve Veritabanı Teknolojileri

FastAPI ile API yazmayı öğrendin. Peki bunu **profesyonel** bir sisteme çevirmek için başka neler lazım? İşte Backend geliştiricinin silahları:

## 1. Veritabanları (Databases) 💾

### A) İlişkisel (SQL) Veritabanları
Tablolar, sütunlar ve satırlar vardır. Disiplinlidir.
*   **PostgreSQL (Lider):** 👑 Şu an dünyada ve FastAPI ile en çok kullanılan veritabanı. Çok güçlüdür, hata affetmez. MySQL'den daha gelişmiştir.
*   **MySQL:** Okullarda ve eski projelerde çok yaygındır. Öğrenmesi kolaydır.
*   **SQLite:** (Bizim Kullanacağımız) Sunucu kurulumu gerektirmez, tek bir dosyadır (`db.sqlite`). Öğrenmek ve küçük projeler için mükemmeldir.

### B) İlişkisel Olmayan (NoSQL) Veritabanları
Tablo yok, JSON gibi esnek yapı var.
*   **MongoDB:** Python sözlükleri gibi çalışır. Veri yapısı sürekli değişen projeler için harikadır.
*   **Redis:** Veriyi diskte değil RAM'de tutar. Şimşek hızındadır. Genelde "Önbellek" (Cache) yapmak için kullanılır.

---

## 2. ORM (Object Relational Mapping) 🌉
"Ben SQL kodu (`SELECT * FROM...`) yazmak istemiyorum, Python kodu yazayım (`User.get_all()`), o arka planda SQL'e dönüşsün" diyorsan ORM kullanmalısın.

*   **SQLAlchemy:** Python dünyasının standardıdır. En kapsamlısı.
*   **Tortoise ORM:** Async (asenkron) olduğu için FastAPI ile çok iyi anlaşır.

---

## 3. Güvenlik ve Kimlik (Auth) 🔐
*   **JWT (JSON Web Tokens):** Kullanıcı giriş yaptığında ona şifreli bir kimlik kartı (Token) verirsin. Her isteğinde o kartı gösterir.
*   **OAuth2:** "Google ile Giriş Yap" butonunun arkasındaki teknolojidir.

---

## 4. Yayınlama ve Paketleme (DevOps) 📦
*   **Docker:** Projeni (Python sürümü, kütüphaneler, veritabanı) bir "Konteyner" içine hapsedersin. "Benim bilgisayarımda çalışıyordu" sorununu bitirir.
*   **Nginx:** Gelen trafiği yöneten (Trafik Polisi) sunucu yazılımı.

---

## 🗺️ Önerilen Öğrenme Sırası
1.  **SQLite + SQLAlchemy:** (Hemen şimdi yapabiliriz)
2.  **PostgreSQL:** (Orta seviye backend)
3.  **Docker:** (Projeni paketlemek için)
4.  **MongoDB:** (Alternatif veritabanı vizyonu için)

---

## 5. Olmazsa Olmaz Python Kütüphaneleri (Çanta) 🎒

Bir Backend geliştiricinin alet çantasında bunlar kesinlikle olmalı:

| Kategori | Kütüphane | Ne İşe Yarar? |
| :--- | :--- | :--- |
| **Web Framework** | `FastAPI` / `Django` | Web sitesinin beynidir. (Zaten öğreniyorsun) |
| **Server** | `Uvicorn` | Yazdığın kodu canlıya (yayıma) alır. |
| **Veritabanı (ORM)** | `SQLAlchemy` | Python kodunu SQL'e çevirir. |
| **Veri Doğrulama** | `Pydantic` | Gelen verinin (E-posta, Şifre) düzgün olup olmadığını kontrol eder. |
| **Göç (Migration)** | `Alembic` | Veritabanında bir sütun ekleyip çıkarırken verilerin silinmemesini sağlar. |
| **Güvenlik (Auth)** | `Python-Jose` (JWT) | Giriş yapma (Login) işlemlerini güvenli hale getirir. |
| **İstek Atma** | `Requests` / `Httpx` | Başka bir siteye (örn: Google Maps) bağlanıp veri çekmeni sağlar. |
| **Test** | `Pytest` | Kodun düzgün çalışıp çalışmadığını otomatik test eder. |
| **Arkaplan İşleri** | `Celery` | E-posta göndermek gibi uzun süren işleri arka planda yapar. |
| **Çevre Değişkenleri**| `Python-Dotenv` | Gizli şifreleri kodun içine değil, gizli bir dosyaya (.env) koymanı sağlar. |

