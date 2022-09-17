
sayi = int(input("Lütfen Bir Sayı Yazınız: "))

def binary(n):
    output = ""
    while n > 0:
        output = "{}{}".format(n % 2, output)
        n = n // 2
    return output

print(binary(sayi))