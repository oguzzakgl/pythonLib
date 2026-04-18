# GitHub Staj İş Akışı

Stajda bir takımla çalışırken kullanacağın standart akış.

---

## Senaryo: Şirkette Bir Göreve Başlamak

```
Görev: "Kullanıcı giriş sayfasına şifremi unuttum butonu ekle"
```

---

## Adım Adım Akış

### 1. Repo'yu al

```bash
# Şirketin repo'sunu fork et (GitHub.com'da yapılır)
# Sonra kendi fork'unu klonla:
git clone https://github.com/SENIN_KULLANICIN/proje.git
cd proje

# Orijinal repo'yu "upstream" olarak ekle
git remote add upstream https://github.com/SIRKET/proje.git
git remote -v   # kontrol et
```

---

### 2. Feature branch aç

```bash
git checkout main
git pull upstream main          # Güncel main'i al
git checkout -b feature/sifremi-unuttum
```

---

### 3. Kodla, commitle

```bash
# ... kod yaz ...

git status
git add .
git commit -m "feat: şifremi unuttum butonu eklendi"
git commit -m "fix: buton mobilde görünmüyordu"
```

**İyi commit mesajı formatı:**
```
feat: yeni özellik
fix: hata düzeltme
docs: dokümantasyon
style: format değişikliği (kod mantığı değişmedi)
refactor: yeniden yapılandırma
test: test ekleme
```

---

### 4. GitHub'a gönder

```bash
git push origin feature/sifremi-unuttum
```

---

### 5. Pull Request (PR) aç

GitHub.com'da:
1. Kendi repo'na git → "Compare & Pull Request" butonu
2. Başlık: `feat: şifremi unuttum butonu eklendi`
3. Açıklama: Ne yaptın, neden yaptın, nasıl test ettiler
4. Reviewer olarak mentor/takım arkadaşını ekle

---

### 6. Code Review sürecinde

```bash
# Reviewer'ın istediği değişikliği yap
git add .
git commit -m "review: buton rengi güncellendi"
git push origin feature/sifremi-unuttum
# PR otomatik güncellenecek
```

---

### 7. Merge sonrası temizle

```bash
git checkout main
git pull upstream main
git branch -d feature/sifremi-unuttum   # Yerel branch sil
```

---

## Sık Yapılan Hatalar

| Hata | Doğrusu |
|---|---|
| Direkt `main`'e push etmek | Her zaman feature branch aç |
| `.env` dosyasını commit'lemek | `.gitignore`'a ekle |
| "son commit" mesajı yazmak | Açıklayıcı mesaj yaz |
| Merge etmeden önce pull çekmemek | `git pull upstream main` → sonra merge |

---

## Takım Repo'sunu Güncel Tutmak

```bash
# Her sabah işe başlarken:
git checkout main
git pull upstream main
git checkout feature/devam-eden-ozellik
git rebase main     # ya da: git merge main
```
