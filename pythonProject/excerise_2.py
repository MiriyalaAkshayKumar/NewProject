# Faulty calculator

#45*3=555, 56+9 = 77, 56/6= 4

opr={"Addition":"+",
     "Subtraction":"-",
     "Multiplication":"*",
     "Division":"/"}
print ("Which of these operations you need to perform:")
print(opr.keys())

A= input("Enter the operator: ")

if A=="Addition":
    B = int(input("Enter first Number :"))
    C = int(input("Enter second Number :"))
# if isnum(B)=False
#     print("Please enter a number")
#     exit()
# if isnum(C)=False
#     print("Please enter a number")
#     exit()

    if B==56:
        if C==9:
            print(" The result is: 77")
        else:
            print("The result is: ")
            print (B+C)
    elif B==9:
        if C==56:
            print(" The result is: 77")
        else:
            print("The result is: ")
            print(B + C)
    else:
        print("The result is: ")
        print(B + C)
elif A=="Subtraction":
    B = int(input("Enter first Number :"))
    C = int(input("Enter second Number :"))
    print("The result is: ")
    print(B - C)
elif A=="Multiplication":
    B = int(input("Enter first Number :"))
    C = int(input("Enter second Number :"))
    if B==45:
        if C==3:
            print(" The result is: 555")
        else:
            print("The result is: ")
            print (B*C)
    elif B==3:
        if C==45:
            print(" The result is: 555")
        else:
            print("The result is: ")
            print(B * C)
    else:
        print("The result is: ")
        print(B * C)
elif A=="Division":

    B = int(input("Enter first Number :"))
    C = int(input("Enter second Number :"))
    if B==56:
        if C==6:
            print(" The result is: 4")
        else:
            print("The result is: ")
            print (B/C)
    else:
        print("The result is: ")
        print(B / C)