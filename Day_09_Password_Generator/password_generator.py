import random
chars='''`~1234567890!@#$%^&*_+-=qwertyuiopQWERTYUIOPasdfghjklzxcvbnm,.;'ASDFGHJKL:"zxcvbnm,.ZXCVBNM<>?'''
length=int(input("enter length: "))
password=""

for a in range(length):
    password+=random.choice(chars)
print(password)