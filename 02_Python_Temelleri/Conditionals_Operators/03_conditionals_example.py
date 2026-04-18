# Vize notunu al
vize = int(input("Vize notunuzu giriniz: "))

# Vize notu 0-100 aralığında değilse uyarı ver ve çık
if vize < 0 or vize > 100:
    print("Hata: Vize notu 0 ile 100 arasında olmalıdır.")
else:
    # Final notunu al
    final = int(input("Final notunuzu giriniz: "))

    # Final notu 0-100 aralığında değilse uyarı ver ve çık
    if final < 0 or final > 100:
        print("Hata: Final notu 0 ile 100 arasında olmalıdır.")
    else:
        # Ortalama hesapla
        ortalama = vize * 0.4 + final * 0.6

        # Sonuç yazdır
        
        # {:.2f} ifadesi, sayıyı virgülden sonra 2 basamak gösterecek şekilde formatlar
        
        if ortalama < 50:
            # İlk print ifadesinde 'f' eksikti, eklendi.
            print(f"Dersten kaldınız. Notunuz: {ortalama:.2f}")
        else:
            # Eğer ortalama 50'den küçük değilse (yani >= 50 ise)
            # ve notlar 0-100 aralığında girildiği için ortalama 100'den büyük olamaz.
            # Bu nedenle tek bir 'else' bloğu yeterlidir.
            # (Senin kodundaki 'elif ortalama 100 >= ortalama >= 50:' koşulu düzeltildi)
            print(f"Tebrikler, dersten geçtiniz. Notunuz: {ortalama:.2f} ")