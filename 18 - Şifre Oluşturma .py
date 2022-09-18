import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
 
password_len = int(input("Şifreniz kaç karakter olsun : "))
password_count = int(input("Kaç tane şifre oluşturulsun : "))
for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password      = password + password_char
        print("Şifre : " , password)