vize = int(input("Lütfen vize notunuzu giriniz: "))
final = int(input("Lütfen final notunuzu giriniz: "))
notunuz = (vize * (0.40)) + (final * (0.60))
if (notunuz >= 50) and (final >= 50) :
    print("Teprikler Dersi Geçtiniz. Notunuz: ", notunuz)
    if(notunuz >=90):
        print("Harf Notunuz:  AA")
    elif(notunuz>=85):
        print("Harf Notunuz:  BA")
    elif(notunuz>=80):
        print("Harf Notunuz:  BB")
    elif(notunuz>=75):
        print("Harf Notunuz:  CB")
    elif(notunuz>=70):
        print("Harf Notunuz:  CC")
    elif(notunuz>=65):
        print("Harf Notunuz:  DC")
    elif(notunuz>=60):
        print("Harf Notunuz:  DD")
    elif(notunuz>=55):
        print("Harf Notunuz:  FF")
else :
        print("Bütünleme sınavına girmeniz gerekmektedir.")

büt =  int(input("Lütfen bütünleme sınav notunuzu giriniz: "))
yeni_not = (vize * (0.40)) + (büt * (0.60))
if yeni_not >= 50 :
    print("Dersi geçtiniz. Notunuz:", yeni_not)
    if(yeni_not >=90):
        print("Harf Notunuz:  AA")
    elif(yeni_not>=85):
        print("Harf Notunuz:  BA")
    elif(yeni_not>=80):
        print("Harf Notunuz:  BB")
    elif(yeni_not>=75):
        print("Harf Notunuz:  CB")
    elif(yeni_not>=70):
        print("Harf Notunuz:  CC")
    elif(yeni_not>=65):
        print("Harf Notunuz:  DC")
    elif(yeni_not>=60):
        print("Harf Notunuz:  DD")
    elif(yeni_not>=55):
        print("Harf Notunuz:  FF")
else :
        print("Dersten kaldınız fakat daha iyi öğrenmek için iyi bir fırsat")        