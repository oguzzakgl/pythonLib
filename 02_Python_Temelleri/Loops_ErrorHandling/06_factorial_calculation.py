# Konu: FaktÃ¶riyel Hesaplama
# AmaÃ§: While dÃ¶ngÃ¼sÃ¼ kullanarak bir sayÄ±nÄ±n faktÃ¶riyelini hesaplamak.

result=1
i=1
number=int(input("FaktÃ¶riyelini hesaplamak istediÄŸiniz sayÄ±yÄ± giriniz: "))
while i<=number:
    result*=i
    i+=1
print(f"{number}! = {result}")
# ÖZET: Bir sayının faktöriyelini hesaplayan matematiksel mantığı, döngüsel bir çarpım işlemiyle adım adım kurgulamayı öğreniyoruz.
