
ogrenci = input("Öğrenciyseniz [E] Değilseniz [H] yazınız: ")
km = int(input("Kaç Km gideceksiniz: "))
ucret = 2.0
ucret_1 = 3.0

if ogrenci == 'E' or ogrenci == 'e' :
  sonuc = ucret*km
  sonuc = float(sonuc)
  print("Toplam Ödemeniz Gereken: ", sonuc ,  "TL")
  print("Bizleri Tercih Ettiğiniz İçin Teşekkür Ederiz")
elif ogrenci == 'H' or ogrenci == 'h'  :
  sonuc_1 = ucret_1 *km
  sonuc_1 = float(sonuc_1)
  print("Toplam Ödemeniz Gereken: ", sonuc_1 , "TL")
  print("Bizleri Tercih Ettiğiniz İçin Teşekkür Ederiz")
