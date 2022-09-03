vize = int(input("Lütfen vize notunuzu giriniz: "))
final = int(input("Lütfen final notunuzu giriniz: "))
notunuz = (vize * (0.40)) + (final * (0.60))
if (notunuz >= 50) and (final >= 50) :
    print("Teprikler Dersi Geçtiniz. Notunuz: ", notunuz)
else :
        print("Bütünleme sınavına girmeniz gerekmektedir.")

büt =  int(input("Lütfen bütünleme sınav notunuzu giriniz: "))
yeni_not = (vize * (0.40)) + (büt * (0.60))
if yeni_not >= 50 :
    print("Dersi geçtiniz. Notunuz:", yeni_not)
else :
        print("Derten kaldınız fakat daha iyi öğrenmek için iyi bir fırsat")