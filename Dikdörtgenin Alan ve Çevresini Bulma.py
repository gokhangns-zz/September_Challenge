Kısa_Kenar = int(input("Lütfen Dikdörtgenin Kısa Kenarını Giriniz: "))
Uzun_Kenar = int(input("Lütfen Dikdörtgenin Uzun Kenarını Giriniz: "))
if Kısa_Kenar < Uzun_Kenar :
    alan = (Kısa_Kenar * Uzun_Kenar)
    cevre = 2*(Kısa_Kenar + Uzun_Kenar)
    print("Dikdörtgenin Alanı: ", alan )
    print("Dikdörtgenin Çevresi: ", cevre)
else :
    print("Lütfen Kenarları Kontrol Edip, Tekrar Deneyiniz!")