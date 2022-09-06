ilk_sayi = int(input("Lütfen ilk sayıyı giriniz: "))
ikinci_sayi = int(input("Lütfen ikinci sayıyı giriniz: "))

if ilk_sayi > ikinci_sayi:
    print("ilk Sayı Büyüktür",ilk_sayi)
elif ilk_sayi < ikinci_sayi:
    print("İkinci Sayı Büyüktür", ikinci_sayi)
else:
    print("Her İki Sayı Eşittir", ilk_sayi, ikinci_sayi)