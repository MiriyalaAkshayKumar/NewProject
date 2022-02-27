print("This for finding the Palindrome Number")

number = int(input("Enter the Number to find whether Palindrome or not \n"))
temp=number
reverse = 0

while(number  >0):
    dig = number%10
    reverse = reverse*10 +dig
    number=number//10

if temp == reverse:
    print("This is the Palindrome number")
else:
    print("This is not Palindrome number")
