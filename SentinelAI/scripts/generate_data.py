from faker import Faker
import random
import uuid
import json
from datetime import datetime

# Faker kütüphanesini kullanarak gerçekçi ama sahte veri üretme motoru.
# 'tr_TR' yerelleştirmesi ile Türkiye'ye özgü isim, şehir ve adres verileri oluşturulabilir.
fake = Faker('tr_TR')

# --- VERİ ÜRETİM MANTIĞI ---
# Bu dosyada aşağıdaki görevleri yerine getirecek fonksiyonlar yazılacak:
# 1. Rastgele bir kullanıcı profili oluşturma (Kredi kartı no, harcama limiti vb.).
# 2. Bu kullanıcı için finansal işlemler (Transactions) üretme.
# 3. Bilinçli olarak "Şüpheli" (Fraud) işlemler enjekte etme (Test senaryoları için).

# --- ÇIKTI FORMATI ---
# Üretilen veriler JSON formatında API'ye gönderilecek veya veritabanına doğrudan kaydedilecek.

if __name__ == "__main__":
    # Test amaçlı birkaç örnek verinin konsola yazdırılması
    pass
