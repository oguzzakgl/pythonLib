# 🌐 Python ile API Kullanımı (Requests)
# Python'da internetten veri çekmek için 'requests' kütüphanesi kullanılır.

# 📦 Kurulum:
# pip install requests

import requests

print("--- API REHBERİ ---")

# ==========================================
# 🚀 1. GET İsteği (Veri Çekme)
# ==========================================
print("\n--- 1. GET İsteği ---")
# Örnek bir ücretsiz API kullanalım (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# Status Code: 200 (OK), 404 (Not Found), 500 (Server Error)
print(f"Durum Kodu: {response.status_code}")

if response.status_code == 200:
    print("Bağlantı Başarılı!")
    data = response.json() # Gelen JSON verisini Python sözlüğüne çevirir
    print(f"Gelen Başlık: {data['title']}")
    print(f"Tam Veri:\n{data}")
else:
    print("Bir hata oluştu.")


# ==========================================
# 📤 2. POST İsteği (Veri Gönderme)
# ==========================================
print("\n--- 2. POST İsteği ---")
# Sunucuya yeni veri eklemek için kullanılır.

post_url = "https://jsonplaceholder.typicode.com/posts"

yeni_veri = {
    "title": "Python ile API Testi",
    "body": "Requests kütüphanesi öğreniyorum.",
    "userId": 1
}

# json parametresi ile veriyi gönderiyoruz
response_post = requests.post(post_url, json=yeni_veri)

print(f"Durum Kodu: {response_post.status_code}") # Genellikle 201 (Created) döner
print("Sunucudan Gelen Cevap:")
print(response_post.json())


# ==========================================
# ❓ 3. Query Parametreleri (Filtereleme)
# ==========================================
print("\n--- 3. Parametre Kullanımı ---")
# URL sonuna ?key=value eklemek yerine params kullanırız.

search_url = "https://jsonplaceholder.typicode.com/comments"
params = {
    "postId": 1 # Sadece 1. postun yorumlarını getir
}

response_search = requests.get(search_url, params=params)

print(f"İstek Yapılan URL: {response_search.url}")
data_search = response_search.json()
print(f"Bulunan Yorum Sayısı: {len(data_search)}")


# ==========================================
# 🛡️ 4. Hata Yakalama (Try-Except)
# ==========================================
print("\n--- 4. Hata Yönetimi ---")

hatali_url = "https://jsonplaceholder.typicode.com/yanlis-adres"

try:
    resp = requests.get(hatali_url, timeout=5) # 5 saniye bekle
    resp.raise_for_status() # Eğer hata kodu (4xx, 5xx) varsa hata fırlat
    print("Veri:", resp.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP Hatası Yakalandı: {err}")
except requests.exceptions.ConnectionError:
    print("Bağlantı Hatası! İnternetini kontrol et.")
except Exception as e:
    print(f"Bilinmeyen bir hata: {e}")
