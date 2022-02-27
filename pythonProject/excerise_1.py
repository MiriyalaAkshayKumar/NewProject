
print("Select the operator")
op ={"Addition":"+" , "Subtraction":"-" , "Mutliplication":"*", "Division":"/"}
print(op.keys())
operation =input("enter the operator")
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
if operation== "Addition":
    if num1==56 and num2==9 or num1==9 and num2==56:
        print("Result==77")
    else:
        print(num1+num2)
if operation=="Subtraction":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("Result==97")
    else:
        print(num1 - num2)
if operation=="Mutliplication":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("Result==777")
    else:
        print(num1 * num2)
if operation=="Division":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("Result==333")
    else:
        print(num1 / num2)




