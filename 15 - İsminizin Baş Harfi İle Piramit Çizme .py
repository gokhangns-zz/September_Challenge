adiniz  =input("Lütfen Adınızı Yazınızı: ")
print("Hoşgeldiniz", adiniz)

ad  = adiniz[0]
add = len(adiniz)
for i in range(add):
    print(' '*(add-i-1) + '*'*(2*i+1))