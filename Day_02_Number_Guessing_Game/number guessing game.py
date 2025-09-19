# how to create random number guessing game
# used random library
import random

Cnumber=random.randrange(1,101)
userInput=int(input("Enter Your Number : "))

if userInput>Cnumber: 
    print("Computer Number",Cnumber)
    print("Your guess number is too high")
elif Cnumber>userInput:
    print("Coputer Number",Cnumber)
    print("Your guess number is too low ")
else:
    print("Computer Number",Cnumber)
    print("Your guess number is equal")