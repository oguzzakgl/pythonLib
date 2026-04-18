# Konu: Dosya Okuma ve Hata YÃ¶netimi
# AmaÃ§: open() fonksiyonu modlarÄ± (r, w, a), with bloÄŸu kullanÄ±mÄ± ve try-except ile hata yakalama.

"""
    open() fonksiyonu ile dosya aÃ§ma ve kapama iÅŸlemleri
    open(dosya adi, dosya_erisim_modu)
    dosya_erisim_modu: 
        'r' : okuma modu (varsayÄ±lan)
        'w' : yazma modu (dosya yoksa oluÅŸturur, varsa iÃ§eriÄŸini siler)
        'a' : ekleme modu (dosya yoksa oluÅŸturur, varsa sonuna ekler)
        'b' : ikili mod (binary)
        't' : metin modu (varsayÄ±lan)
        '+' : okuma ve yazma modu

"""

f = open("log.txt", encoding="utf-8")
print(f.read())
f.close()


with open("log.txt", encoding="utf-8") as f:
    print(f.read(10))
    print(f.tell())
    print(f.read())
    print(f.tell())
try:
    with open("log2.txt", "r", encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("Dosya bulunamadÄ±." + str(e))



# ÖZET: Dosyalarý okuma modunda (r) açmayý, 'with' bloðu ile güvenli dosya yönetimini ve dosya bulunamadýðýnda programýn çökmemesi için hata yakalamayý öðreniyoruz.
