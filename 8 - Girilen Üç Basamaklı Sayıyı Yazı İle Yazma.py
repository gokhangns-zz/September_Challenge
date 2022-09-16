dict_b = {1:"bir", 2:"iki", 3:"üç", 4:"dört", 5:"beş", 6:"altı", 7:"yedi", 8:"sekiz", 9:"dokuz", 0:""}
dict_o = {1:"on", 2:"yirmi", 3:"otuz", 4:"kırk", 5:"elli", 6:"altmış", 7:"yetmiş", 8:"seksen", 9:"doksan", 0:""}
dict_y = {1:"yüz", 2:"ikiyüz", 3:"üçyüz", 4:"dörtyüz", 5:"beşyüz", 6:"altıyüz", 7:"yediyüz", 8:"sekizyüz", 9:"dokuzyüz", 0:""} 

sayiniz = input("Lütfen Üç Basamaklı Sayı Giriniz: ")
birler = int(sayiniz[2])
onlar = int(sayiniz[1])  
yüzler = int(sayiniz[0])

print(dict_y[yüzler] + dict_o[onlar] + dict_b[birler])

