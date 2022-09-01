import datetime as dt
dogum_tarihi = input("Doğum Tarihinizi Yıl Olarak Giriniz:  ")
dogum_tarihi = dt.datetime.strptime(dogum_tarihi,"%Y")
simdiki_tarih = dt.datetime.now()
fark = simdiki_tarih - dogum_tarihi
Yıl = fark.days // 365
print(f"{Yıl} Yaşındasınız")