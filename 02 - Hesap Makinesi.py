from re import A


def Topla(x, y):
   return x + y

def Cikar(x, y):
   return x - y
 
def Carp(x, y):
   return x * y
 
def Bol(x, y):
   return x / y
 
print("Yapılacak İşlemi Seçin: \n 1.Toplama \n 2.Çıkarma \n 3.Çarpma \n 4.Bölme")

Yapilacak_İslemi_Secin = input("Seçiminiz (1/2/3/4):")
A = Yapilacak_İslemi_Secin
 
ilk_Sayi = int(input("1. Sayı: "))
B = ilk_Sayi
ikinci_Sayi = int(input("2. Sayı: "))
C = ikinci_Sayi
if A  == '1':
   print(B,"+",C,"=", Topla(B,C))
 
elif A  == '2':
   print(B,"-",C,"=", Cikar(B,C))
 
elif A  == '3':
   print(B,"*",C,"=", Carp(B,C))
 
elif A  == '4':
   print(B,"/",C,"=", Bol(B,C))
else:
   print("Geçersiz İşlem")