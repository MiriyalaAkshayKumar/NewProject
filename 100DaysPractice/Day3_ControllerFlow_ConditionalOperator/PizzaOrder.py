print("Welcome to Pizza Deliveries")
size=input("What type of Pizza do you want? S,M,L : ")
add_pepperoni=input("Would you like to add pepperoni Y or N : ")
add_cheese=input("Would you like to add cheese Y or N : ")
bill =0

if size == "S":
    bill+=15
elif size == "M":
    bill+=20
else :
    bill+=25

if add_pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
if add_cheese == "Y":
    bill+=1

print(f"Your final bill: {bill}")


