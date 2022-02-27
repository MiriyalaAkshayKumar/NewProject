height=(input("Please enter your height in m: "))
weight=(input("Please enter your weight in kg: "))

BMI=int(weight)/float(height)* float(height)
#f-String
print(f"Your Ideal weight should be:{int(BMI)}")
