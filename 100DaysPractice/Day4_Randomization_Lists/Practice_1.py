import random
print("Welcome to pay bill")

#Akshay,Manoj,Sai,Vamshi,Nikilesh,Lalith

Enter_names=input("Enter the names: ")
names=Enter_names.split(",")
print(names)
len(names)
# split=random.randint(0,5)
Person_who_will_pay=random.choice(names)
print(Person_who_will_pay+" "+ "Will pay the bill!")