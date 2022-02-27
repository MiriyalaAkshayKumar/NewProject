print("Prime Number Checker")

number = int(input("Enter number to check whether prime or not: "))

def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number % i ==0:
            is_prime=False
    if is_prime:
        print("Its a prime number")
    else:
        print("Its not a prime number")


prime_checker(number)
