# VeritabanÄ± Ä°ÅŸlemleri (SQLite)
import sqlite3



def baglan():
    con = sqlite3.connect("stok.db")
    cursor = con.cursor()
    return con, cursor

def tablolari_kur():
    con, cursor = baglan()
    cursor.execute("CREATE TABLE IF NOT EXISTS urunler (id INTEGER PRIMARY KEY, ad TEXT, fiyat REAL, stok INTEGER)")
    con.commit()
    con.close()

def urun_ekle(ad, fiyat, stok):
    con, cursor = baglan()
    cursor.execute("INSERT INTO urunler (ad, fiyat, stok) VALUES (?, ?, ?)", (ad, fiyat, stok))
    con.commit()
    con.close()

def urunleri_getir():
    con, cursor = baglan()
    cursor.execute("SELECT * FROM urunler")
    veriler = cursor.fetchall()
    con.close()
    return veriler

if __name__ == "__main__":
    tablolari_kur()
    urun_ekle("urun1", 10, 10)
    urun_ekle("urun2", 20, 20)
    urun_ekle("urun3", 30, 30)
# ÖZET: SQLite kullanarak veritabaný baðlantýsý kurma, tablo oluþturma ve SQL sorgularýyla veri çekme/ekleme iþlemlerini bir modül yapýsý içerisinde organize ediyoruz.
