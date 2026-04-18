# W14 - Mini Proje: Stok Analiz Sistemi

Bu proje, Python öğrenme sürecinde edinilen **SQL**, **Pandas** ve **Algoritma** becerilerini birleştiren kapsamlı bir uygulamadır.

## 🎯 Proje Hedefi
Sıfırdan çalışan, veritabanı bağlantılı ve veri analizi yapabilen bir sistem mimarisi kurmak.

## 🏗️ Proje Mimarisi

Sistem 3 ana katmandan oluşur:

### 1. Backend (Veri Katmanı) - `database.py`
Projenin hafızasıdır.
- **Teknoloji**: `sqlite3`
- **Görevler**:
    - `stok.db` veritabanına bağlanır.
    - `urunler` tablosunu oluşturur.
    - Ürün ekleme ve listeleme fonksiyonlarını barındırır.

### 2. Frontend (Kullanıcı Arayüzü) - `main.py`
Kullanıcı ile etkileşime giren katmandır.
- **Teknoloji**: Python Terminal (CLI)
- **Görevler**:
    - Kullanıcıya menü sunar (Ekle, Listele, Çıkış).
    - Kullanıcıdan aldığı verileri `database.py` üzerinden veritabanına kaydeder.

### 3. Analiz (Raporlama) - `analiz.py`
Veriyi bilgiye dönüştüren katmandır.
- **Teknoloji**: `pandas`
- **Görevler**:
    - Veritabanındaki tüm ürünleri çeker.
    - Kritik stok seviyesindeki (20'den az) ürünleri raporlar.
    - Fiyat analizleri sunar.

## 🚀 Çalıştırma

Önce veri girişi yapmak için ana uygulamayı çalıştırın:
```bash
python main.py
```

Raporları görmek için analiz modülünü çalıştırın:
```bash
python analiz.py
```
