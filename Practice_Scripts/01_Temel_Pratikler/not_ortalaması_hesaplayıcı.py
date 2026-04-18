# --- Gelişmiş Not Hesaplama (Hata Yakalamalı ve Döngülü) ---

# Ana döngü
while True:
    
    # Hata yakalama
    try:
        
        # Vize notu giriş
        vize = int(input("Vize Notunuzu Giriniz: "))

        # Geçerlilik kontrolü
        if vize < 0 or vize > 100:
            print("Hata: Notunuz 0 ile 100 arasında olmalıdır.")
            # 'continue' -> Döngünün başına dön (tekrar vize notu iste)
            continue 

        # Final notu giriş
        final = int(input("Final Notunuzu Giriniz: "))
        
        # Geçerlilik kontrolü
        if final < 0 or final > 100:
            print("Hata: Notunuz 0 ile 100 arasında olmalıdır.")
            continue # Döngünün başına dön (tekrar vize notu iste)
            
        # Ortalama hesapla
        ortalama = vize * 0.4 + final * 0.6
        
        print(f"\nNot Ortalamanız: {ortalama:.2f}")

        # Harf notu hesaplama
        final_baraji = 50
        if final < final_baraji:
            print(f"Durum: Final notunuz barajın ({final_baraji}) altında.")
            print(f"Ortalamanız {ortalama:.2f} olsa bile dersten KALDINIZ. Harf Notu: FF")
        
        elif ortalama < 50:
            print(f"Durum: Dersten Kaldınız. Harf Notunuz: FF")
        elif ortalama < 60:
            print("Durum: Tebrikler! Dersten DD notuyla geçtiniz.")
        elif ortalama < 70:
            print("Durum: Tebrikler! Dersten DC notuyla geçtiniz.")
        elif ortalama < 80:
            print("Durum: Tebrikler! Dersten CC notuyla geçtiniz.")
        elif ortalama < 90:
            print("Durum: Tebrikler! Dersten BB notuyla geçtiniz.")
        else:
            print("Durum: Tebrikler! Dersten AA notuyla geçtiniz.")

    except ValueError:
        print("\nHata: Lütfen sadece sayısal bir değer giriniz (Örn: 80).")
        
    
    # Devam kontrolü
    print("-" * 30)
    devam = input("Başka bir not hesaplamak ister misiniz? (E/H): ").lower()
    
    if devam != 'e':
        print("Program sonlandırıldı. İyi günler!")
        break # 'while True' döngüsünü kır ve programı bitir
    
    print("\n" + "=" * 30 + "\n") # Yeni hesaplama için ayraç
# �ZET: Vize ve final notlar�n� alarak ortalama ve harf notu hesaplayan, final baraj� kontrol� yapan ve hatal� giri�leri filtreleyen etkile�imli bir ��renci not sistemi kurguluyoruz.
