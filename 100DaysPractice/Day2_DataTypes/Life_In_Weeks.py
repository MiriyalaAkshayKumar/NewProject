age=(input("Enter your age: "))
print(f"This is print age: {age}")

int_age= int(age)
years_remaining_age=90-int_age
days_remaining=years_remaining_age*365
weeks_remaining=years_remaining_age*52
months_remaing=years_remaining_age*12

message=f"You have {days_remaining} Days, {weeks_remaining} weeks, {months_remaing} months left"
print(message)
