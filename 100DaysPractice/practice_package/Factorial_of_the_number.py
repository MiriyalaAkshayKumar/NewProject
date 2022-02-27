print("This program is for finding the Factorial of the number")

Number = int(input("Enter the number : \n"))
fact =1

if Number == 0:
    print(f"Factorial Zero is {Number}")
elif Number == 1:
    print(f"Factorial 1 is {Number}")
else:
    while(Number > 0):
        fact*= Number
        Number -= 1
    print(f"Factorial of given number is : {fact} ")
