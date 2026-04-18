#girilen karakter harfmi, harfse büyük mü küçük mü sesli mi sessiz mi kontrolü

char = input("Bir karakter giriniz: ")
if char.isalpha():  # Harf kontrolü
    if char.isupper():  # Büyük harf kontrolü
        if char.lower() in 'aeıioöuü':  # Sesli harf kontrolü
            print(f"Girilen karakter '{char}' büyük sesli bir harftir.")
        else:
            print(f"Girilen karakter '{char}' büyük sessiz bir harftir.")
    else:  # Küçük harf
        if char in 'aeıioöuü':  # Sesli harf kontrolü
            print(f"Girilen karakter '{char}' küçük sesli bir harftir.")
        else:
            print(f"Girilen karakter '{char}' küçük sessiz bir harftir.")
else:
    print("Girilen karakter bir harf değildir.")