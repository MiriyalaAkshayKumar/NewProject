import random

print("This program is for Generating the password")

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')','-','_','+','<','>','?','/','.',',','[',']','{','}']
numbers=['1','2','3','4','5','6','7','8','9','0']

no_letters=int(input("Enter the letters would you like to add in passwords: \n"))
no_symbols=int(input("Enter the symbols would you like to add in passwords: \n"))
no_numbers=int(input("Enter the numbers would you like to add in passwords: \n"))

#Easy Way
print("---------Easy way------")
password=""
for char in range(1,no_letters+1):
    password+=random.choice(letters)
for char in range(1,no_symbols+1):
    password+=random.choice(symbols)
for char in range(1,no_numbers):
    password+=random.choice(numbers)

print(password)

#Hard Way
print("----Hard way-------")
password1=[]
for char in range(1,no_letters+1):
    password1+=random.choice(letters)
for char in range(1,no_symbols+1):
    password1+=random.choice(symbols)
for char in range(1,no_numbers):
    password1+=random.choice(numbers)

random.shuffle(password1)
print(password1)
