# Git Referans Kılavuzu

Staj ve proje süreçlerinde sık kullanılan Git komutları.

---

## 📁 Dosya İçeriği

| Dosya | Konu |
|---|---|
| `01_temel_komutlar.md` | init, add, commit, push, pull |
| `02_branch_merge.md` | Branch açma, merge, conflict çözme |
| `03_github_is_akisi.md` | Fork → Clone → PR iş akışı (staj senaryosu) |

---

## ⚡ En Çok Kullanılan Komutlar (Hızlı Bakış)

```bash
git status                    # Değişiklikleri gör
git add .                     # Tümünü hazırla
git commit -m "mesaj"         # Kaydet
git push origin main          # GitHub'a gönder
git pull origin main          # GitHub'dan çek
git log --oneline             # Geçmişi gör
```

---

## 🏢 Stajda Tipik İş Akışı

```
1. Repo'yu fork et (GitHub'da)
2. git clone <url>
3. git checkout -b feature/yeni-özellik
4. Kod yaz → git add → git commit
5. git push origin feature/yeni-özellik
6. GitHub'da Pull Request aç
7. Code review → merge
```
