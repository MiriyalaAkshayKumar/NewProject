print("BMI Calculator")
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
BMI = weight/height**2
print(f"Your BMI {float(round(BMI,2))}")

if BMI < 18.5:
    print("Your are under weight")
elif BMI  < 25:
    print("Your Normal weight")
elif BMI < 30:
    print("Your Over weight")
elif BMI < 35:
    print("Your Obese")
else:
    print("Clinically Obese")

