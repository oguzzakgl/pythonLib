# PostgreSQL Nedir?
PostgreSQL (kısaca Postgres), dünyanın en gelişmiş açık kaynaklı **İlişkisel Veritabanı Yönetim Sistemidir** (RDBMS).

## 🚀 Neden PostgreSQL?
1.  **Güçlü ve Güvenilir:** Finansal uygulamalar, devlet sistemleri ve büyük web projelerinde kullanılır.
2.  **Açık Kaynak:** Ücretsizdir ve topluluk tarafından sürekli geliştirilir.
3.  **İleri Özellikler:** JSON verilerini saklayabilir (NoSQL gibi), karmaşık sorguları ve büyük verileri çok hızlı işler.
4.  **Veri Bütünlüğü:** Verilerinizin kaybolmaması veya bozulmaması için (ACID uyumluluğu) çok sıkı kuralları vardır.

## 🆚 SQLite vs PostgreSQL
Biz projeye SQLite ile başladık ama PostgreSQL'e geçtik. Farkları ne?

| Özellik | SQLite | PostgreSQL |
| :--- | :--- | :--- |
| **Kullanım Yeri** | Mobil uygulamalar, küçük projeler, testler | Büyük web siteleri, şirket veritabanları |
| **Kurulum** | Kurulum gerekmez, tek bir dosyadır | Sunucu kurulumu gerektirir |
| **Kullanıcılar** | Aynı anda tek kişi yazabilir | Binlerce kişi aynı anda kullanabilir |
| **Güç** | Basit sorgular için idealdir | Çok karmaşık analizler yapabilir |

## 🛠 Temel Kavramlar (SQL)
*   **Database (Veritabanı):** Tüm tabloların durduğu ana depo (Bizim `coinmind` veritabanımız gibi).
*   **Table (Tablo):** Excel sayfası gibi düşün. Satır ve sütunlardan oluşur (Örn: `market_data` tablosu).
*   **Row (Satır):** Tablodaki her bir kayıt (Örn: BTC'nin şu anki fiyat bilgisi).
*   **Column (Sütun):** Verinin türü (Örn: Fiyat, Tarih, Sembol).

## 🎓 Projemizdeki Rolü
CoinMind projesinde PostgreSQL'i, kripto paraların saniyelik değişen fiyatlarını, hacimlerini ve analiz sonuçlarını **kalıcı ve güvenli** bir şekilde saklamak için kullanıyoruz. Uygulamayı kapatsak bile verilerimiz PostgreSQL sunucusunda güvende kalır.
