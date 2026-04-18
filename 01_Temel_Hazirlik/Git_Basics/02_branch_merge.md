# Branch ve Merge

---

## 1. Branch Nedir?

Ana kodu bozmadan yeni özellik geliştirmek için paralel kopya.

```
main ──●──────────────────●── (merge)
        \                /
feature  ●──●──●──●──●──
```

---

## 2. Branch Komutları

```bash
git branch                        # Tüm branch'leri listele
git branch -a                     # Remote dahil listele

git branch yeni-ozellik           # Branch oluştur
git checkout yeni-ozellik         # Branch'e geç
git checkout -b yeni-ozellik      # Oluştur + geç (kısayol)

git branch -d yeni-ozellik        # Branch sil (merge olduysa)
git branch -D yeni-ozellik        # Zorla sil
```

---

## 3. Merge

```bash
# main branch'e geç, sonra feature'ı merge et
git checkout main
git merge feature/yeni-ozellik

# Merge geçmişi temiz tutmak için --no-ff
git merge --no-ff feature/yeni-ozellik
```

---

## 4. Conflict (Çakışma) Çözme

İki kişi aynı satırı değiştirirse conflict olur:

```python
<<<<<<< HEAD           ← senin değişikliğin
x = 10
=======
x = 20                 ← karşı tarafın değişikliği
>>>>>>> feature/branch
```

**Çözüm:**
1. Dosyayı aç, `<<<`, `===`, `>>>` işaretlerini bul
2. Hangisinin doğru olduğuna karar ver, diğerini sil
3. `git add dosya.py` → `git commit`

---

## 5. Rebase (İleri Seviye)

```bash
# feature branch'ini main'in en güncel haline dayandır
git checkout feature/yeni-ozellik
git rebase main

# Stajda genellikle merge yeterli, rebase opsiyonel
```

---

## 6. Remote Branch İşlemleri

```bash
git push origin feature/yeni-ozellik   # Branch'i GitHub'a gönder
git pull origin main                    # Remote main'i çek
git fetch origin                        # Sadece kontrol et, merge etme
git branch -r                           # Remote branch'leri listele
```

---

## 7. Stajda Branch İsimlendirme Geleneği

```
feature/kullanici-girisi      → yeni özellik
fix/login-hata                → bug düzeltme
hotfix/kritik-guvenlik        → acil düzeltme
docs/api-dokumantasyonu       → dokümantasyon
refactor/veritabani-modeli    → kod iyileştirme
```
