# 🧠 Derinlemesine Analiz: Kodun Arka Planında Neler Dönüyor?

Haklısın! Yazdığımız kod sadece **buzdağının görünen yüzü**. O 30 satırlık kodun arkasında devasa bir mühendislik çalışıyor.

İşte "bu kadar kısa olamaz" dediğin şeylerin arka planı:

---

## 1. SQL Bölümü: `sqlite3`
Sen `connect(":memory:")` yazdığında bilgisayarın arka planda şunları yaptı:

*   **RAM Tahsisi:** İşletim sisteminden (Windows) özel bir RAM bloğu istedi.
*   **Dosya Sistemi Simülasyonu:** Sanki hard diskte bir dosya varmış gibi davranan sanal bir dosya sistemi kurdu.
*   **B-Tree Algoritması:** Verileri (Milyonlarca olsa bile) milisaniyede bulabilmek için verileri "Ağaç Yapısı" (B-Tree) ile dizdi.
*   **ACID Kuralları:** Elektrik kesilse bile verinin bozulmamasını sağlayan (Atomicity, Consistency...) protokolleri hazırladı.

**Sen sadece:** `INSERT` dedin.
**O arka planda:** Veriyi binary (0 ve 1) hale çevirdi, boş bir hafıza bloğu buldu, oraya yazdı ve "Adres Defterine" (Index) bu verinin yerini not etti.

---

## 2. Pandas Bölümü: `read_sql` ve `DataFrame`
Bu kısım tam bir sihirbazlık.

*   **Connector (Köprü):** Pandas, SQL ile konuşmak için C diliyle yazılmış özel bir köprü kurdu.
*   **Type Inference (Tip Tahmini):** SQL'den gelen veriye baktı: "Bu yazı mı? Sayı mı? Tarih mi?" diye analiz etti ve Python tipine çevirdi.
*   **Memory Layout (Hafıza Düzeni):** Veriyi Python'ın hantal listeleri gibi değil, **bloklar halinde** (Columnar Store) RAM'e yerleştirdi. Bu yüzden Pandas, Excel'den 100 kat hızlıdır.

**Sen sadece:** `df[df["stok"] < 20]` dedin.
**O arka planda:** Tüm "Stok" sütununu işlemciye (CPU) gönderdi, tek bir saat vuruşunda (SIMD) hepsini 20 ile karşılaştırdı ve sonucu getirdi.

---

## 3. NumPy Bölümü: `np.mean`
Burası işin matematiği.

*   **C Entegrasyonu:** NumPy Python ile yazılmamıştır! **C ve Fortran** (çok eski ve çok hızlı diller) ile yazılmıştır.
*   **Vektörizasyon:** Sen bir listeyi çarptığında (Döngü ile), Python elemanları tek tek çarpar. NumPy ise tüm listeyi "Tek bir Vektör" olarak işlemciye atar.
*   **Broadcasting:** Boyutları uyuşmayan matrisleri bile (büyük matematiksel kurallarla) birbirine uydurup işlem yapar.

**Sen sadece:** `fiyatlar * 2` dedin.
**O arka planda:** Bellekteki o sayı bloğunun başlangıç adresini aldı, bitiş adresine kadar binary kaydırma (bit shifting) ile ışık hızında çarpma yaptı.

---

### Özetle
Kodun kısa olması seni yanıltmasın. Sen **kaptan köşkünde** oturup "Motorları çalıştır" diyorsun (`import pandas`). Aşağıda makine dairesinde (C, C++, Assembly) ter döken binlerce satırlık kod çalışıyor.

Bu kütüphaneler (SQL, Pandas, NumPy), o zor işleri biz yapmayalım diye var. 😉
