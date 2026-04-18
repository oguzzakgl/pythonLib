# Git Temel Komutlar

---

## 1. İlk Kurulum (Bir Kez Yapılır)

```bash
git config --global user.name  "Adın Soyadın"
git config --global user.email "mail@example.com"
git config --global core.editor "code --wait"   # VS Code varsayılan editör
```

---

## 2. Repo Başlatma

```bash
# A) Sıfırdan başlat
git init
git remote add origin https://github.com/kullanici/repo.git

# B) Mevcut repo'yu klonla
git clone https://github.com/kullanici/repo.git
git clone https://github.com/kullanici/repo.git klasor_adi
```

---

## 3. Temel Döngü (En Çok Kullanılan)

```bash
git status                    # Hangi dosyalar değişti?
git diff                      # Değişikliklerin detayı

git add dosya.py              # Tek dosya ekle
git add .                     # Tüm değişiklikleri ekle
git add -p                    # Değişiklikleri parça parça incele (dikkatli kullan)

git commit -m "kısa açıklama"
git commit -m "başlık" -m "daha uzun açıklama"

git push origin main          # GitHub'a gönder
git pull origin main          # GitHub'dan çek (fetch + merge)
```

---

## 4. Geçmişi İnceleme

```bash
git log                       # Tüm geçmiş
git log --oneline             # Tek satır özet
git log --oneline --graph     # Dal yapısıyla birlikte
git log -n 5                  # Son 5 commit

git show abc1234              # Belirli bir commit'in içeriği
git diff HEAD~1               # Son commit ile öncesini karşılaştır
```

---

## 5. Geri Alma İşlemleri

```bash
# Staged dosyayı unstage yap (git add'i geri al)
git restore --staged dosya.py

# Dosyadaki değişikliği geri al (SON KAYDEDİLEN haline dön)
git restore dosya.py

# Son commit'i geri al (dosyalar korunur)
git reset --soft HEAD~1

# Son commit'i tamamen sil (DİKKAT: değişiklikler kaybolur)
git reset --hard HEAD~1

# Belirli bir commit'e geri dön (güvenli yöntem)
git revert abc1234
```

> ⚠️ `--hard` push edilmiş commitlere uygulanmamalı!

---

## 6. .gitignore

Takip edilmemesi gereken dosyalar:

```
# .gitignore örneği
__pycache__/
*.pyc
.env              ← API anahtarları! Asla commit'leme
.venv/
*.pkl             ← Büyük model dosyaları
*.csv             ← Ham veri dosyaları (büyükse)
.DS_Store
```

---

## 7. Stash (Geçici Saklama)

```bash
git stash           # Değişiklikleri geçici sakla
git stash pop       # Geri getir
git stash list      # Saklanan değişiklikler
```
