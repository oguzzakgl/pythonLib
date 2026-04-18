# Konu: String Formatlama
# AmaÃ§: format() metodu ve f-string kullanÄ±mÄ± ile metinleri biÃ§imlendirmek.

# string formatlama
name = "OÄŸuz"
age = 25
price = 99.9945454
text = "Benim adÄ±m {} ve yaÅŸÄ±m {}.".format(name, age)
print(text)

# f-string formatlama
text_f = f"Benim adÄ±m {name} ve yaÅŸÄ±m {age}."
print(text_f)

text_price = f"ÃœrÃ¼nÃ¼n fiyatÄ±: {price:.2f} TL" # VirgÃ¼lden sonra 2 basamak
print(text_price)   
text_price2 = f"ÃœrÃ¼nÃ¼n fiyatÄ±: {price:,.2f} TL" # Binlik ayraÃ§ ekleme
# ÖZET: Değişkenleri metinlerin içine yerleştirmek için en modern yöntem olan f-string yapısını ve sayısal formatlama tekniklerini öğreniyoruz.
