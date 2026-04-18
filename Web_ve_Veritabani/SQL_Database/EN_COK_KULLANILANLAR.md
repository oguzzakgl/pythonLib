# 🚀 Profesyonel İpuçları: Başka Neler Çok Kullanılır?

Dosyada gördüklerin **%50'lik** kısımdı. Geriye kalan ve sektörde "Olmazsa Olmaz" dediğimiz **diğer %30'luk** kısım şunlardır:

---

## 1. SQL: Gruplama ve Birleştirme 🗄️

### A) `GROUP BY` (Gruplama)
"Her kategoriden kaç ürün var?" veya "Hangi departman toplam ne kadar maaş alıyor?" sorularının cevabıdır.
```sql
SELECT departman, COUNT(*) FROM calisanlar GROUP BY departman;
```

### B) `JOIN` (Birleştirme - EN ÖNEMLİSİ)
Veriler tek tabloda durmaz. `Musteriler` ve `Siparisler` ayrı tablodur. Bunları birleştirmek için kullanılır.
```sql
SELECT * FROM siparisler JOIN musteriler ON siparisler.musteri_id = musteriler.id;
```

### C) `UPDATE` ve `DELETE`
Sadece veri eklemeyiz, bazen düzeltiriz veya sileriz.
```sql
UPDATE urunler SET fiyat = 500 WHERE id = 1;
DELETE FROM urunler WHERE stok = 0;
```

---

## 2. Pandas: Temizlik ve Raporlama 🐼

### A) `groupby()` (Gruplama)
SQL'deki `GROUP BY`'ın aynısıdır.
```python
# Her departmanın ortalama maaşını bul
df.groupby("Departman")["Maas"].mean()
```

### B) `sort_values()` (Sıralama)
Büyükten küçüğe veya A'dan Z'ye sıralama.
```python
df.sort_values(by="Fiyat", ascending=False) # En pahalı en üstte
```

### C) `dropna()` ve `fillna()` (Veri Temizliği)
Gerçek hayatta veriler eksik gelir (Nan).
*   `df.dropna()`: Eksik verisi olan satırı komple siler.
*   `df.fillna(0)`: Eksik yerlere 0 yazar.

### D) `to_excel("rapor.xlsx")`
Yaptığın analizi patronuna atmak için Excel dosyası olarak kaydeder.

---

## 3. NumPy: Şekil Verme ve Rastgelelik 🔢

### A) `np.reshape()`
Verinin şeklini değiştirir. (Örn: 10 elemanlı tek sırayı, 2 satır 5 sütun yap). Yapay zeka için çok kritiktir.

### B) `np.random` (Rastgelelik)
Test verisi üretmek için kullanılır.
*   `np.random.randint(0, 100)`: 0-100 arası rastgele sayı tut.
*   `np.random.choice(["Kırmızı", "Mavi"])`: Listeden rastgele seç.

### C) `np.arange()` ve `np.linspace()`
Otomatik sayı dizileri üretir.
*   `np.arange(0, 10, 2)` -> `[0, 2, 4, 6, 8]`
