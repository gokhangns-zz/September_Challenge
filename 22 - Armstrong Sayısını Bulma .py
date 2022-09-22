#Armstong Sayısı
#Bir sayının basamaklarındaki tüm rakamlarının sayı değerlerinin , 
# sayının basamak sayısı kadar kuvveti alınıp toplanıldığında elde edilen sayı, 
# sayının kendisine eşitse bu sayıya “Armstrong sayısı” denir.

sayi = int(input("Lütfen bir sayı giriniz: "))
numara = 0
temp = numara
while temp > 0:
   digit = temp % 10
   sayi += digit ** 3
   temp //= 10

if numara == sayi:
   print(numara,"Bir Armstrong Sayısıdır.")
else:
   print(numara,"Bir Armstrong Sayısı Değildir.")