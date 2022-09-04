
otobüs_saatleri = [10,11,12,13,14,15,16]
sorgula = input("lütfen otobüs saatini giriniz:")

if [(sorgula == otobüs_saatleri[0]) or (sorgula == otobüs_saatleri[1]) or (sorgula == otobüs_saatleri[2]) or (sorgula == otobüs_saatleri[3]) or (sorgula == otobüs_saatleri[4]) or (sorgula == otobüs_saatleri[5]) or (sorgula == otobüs_saatleri[6])]:
    print ("otobüs saatiniz eşleşti")
else:
    print("yeni bir saat deneyiniz")