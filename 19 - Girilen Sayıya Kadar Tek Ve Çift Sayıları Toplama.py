 
sayiniz = input("Lütfen Bir Sayı Girin: ")
tek_toplam = 0
cift_toplam = 0
for i in range(1,int(sayiniz)) :
  if(i%2==0):
    cift_toplam+=i
  else :
    tek_toplam+=i
print("Tek Sayıların Toplamı : {0}".format(tek_toplam))
print("Çift Sayıların Toplamı : {0}".format(cift_toplam))