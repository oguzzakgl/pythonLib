
# Konu: Dosyaya Yazma (Write)
# AmaÃ§: 'w' modu ile dosya oluÅŸturma ve Ã¼zerine yazma (overwrite) iÅŸlemi.

# w yazma modu
# dosyayÄ± konumda oluÅŸturur
# eÄŸer konumda aynÄ± dosya varsa iÃ§eriÄŸini siler ve yeni oluÅŸturur

# file = open("dosya.txt", "w", encoding="utf-8")

# file.write("Python programlama dili\n")
# file.close()

with open("dosya.txt", "w", encoding="utf-8") as file:
    file.write("Python programlama dili\n")
    file.write("Python 3 programlama dili\n")

with open("dosya.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i, end="")
# ÖZET: 'w' (yazma) modunu kullanarak yeni dosyalar oluþturmayý ve mevcut dosyalarýn üzerine yeni veriler yazarak içeriklerini güncellemeyi pratik ediyoruz.
