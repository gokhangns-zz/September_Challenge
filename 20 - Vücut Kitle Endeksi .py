
boyunuz = float(input("Lütfen Boyunuzu Metre Olarak Yazınız: "))
kilonuz = int(input("Lütfen Kilonuzu Kilogram Olarak Yazınız: "))
 
endeks  = kilonuz / (boyunuz * boyunuz)
 
if endeks <18:
    print("\n zayıf {}".format(endeks))
elif endeks >= 18 and endeks < 25 :
    print("\n normal {}".format(endeks))
elif endeks >= 25 and endeks <30:
    print("\n kilolu {}".format(endeks))
elif endeks >= 30 and endeks <35:
    print("\n obez {}".format(endeks))
else:
    print("\n ciddi obez {}".format(endeks))
 