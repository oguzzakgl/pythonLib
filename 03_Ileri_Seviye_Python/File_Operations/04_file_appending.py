# Konu: Dosyaya Ekleme (Append)
# AmaÃ§: 'a' modu ile mevcut dosyanÄ±n sonuna veri ekleme iÅŸlemi.

# a yazma modu
# dosyayÄ± konumda oluÅŸturur
# eÄŸer konumda aynÄ± dosya varsa iÃ§eriÄŸini silmeden sonuna ekleme

with open("dosya.txt", "a", encoding="utf-8") as file:
    file.write("birinci satir\n")
# ÖZET: Mevcut bir dosyanın içeriğini bozmadan, 'a' (ekleme) modu sayesinde yeni verileri dosyanın en sonuna nasıl ekleyeceğimizi öğreniyoruz.
