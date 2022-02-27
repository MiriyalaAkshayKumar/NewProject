print("Welcome to love calculator")
name1 = input("Enter name one: ")
name2 = input("Enter name two: ")

com_name = name1 + name2
lowercase=com_name.lower()

t=lowercase.count("t")
r=lowercase.count("r")
u=lowercase.count("u")
e=lowercase.count("e")
true = t + r + u + e

l=lowercase.count("l")
o=lowercase.count("o")
v=lowercase.count("v")
e=lowercase.count("e")
love = l + o + v + e

love_score= int(str(love)+str(true))

if(love_score<10) or (love_score>90):
    print(f"{love_score} , Your bonding is like coke and mentos")
elif(love_score>=40) and (love_score<=50):
    print(f"{love_score} , You are alright together")
else:
    print(love_score)
