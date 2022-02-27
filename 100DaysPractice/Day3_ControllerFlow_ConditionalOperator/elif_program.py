print("Welcome to RollerCoast ride")
height = int(input("Enter your height in cm : "))

if height >= 120:
    print("Your eligible to take a ride")
    age = int(input("Enter your age : "))
    if age < 12:
        print("Ticket price is $5")
    elif age <= 18:
        print("Ticket price is $7")
    else:
        print("Ticket price is $12")
else:print("Sorry,you have to grow your height to take a ride")
