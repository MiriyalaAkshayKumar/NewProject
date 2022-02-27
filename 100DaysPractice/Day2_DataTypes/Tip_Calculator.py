print("Welcome to the Tip Calculator")
bill=float(input("What was the Total Bill amount? :$"))
tip= int(input("What percentage tip would you like to give? 10 ,12, or 15:"))
people = int(input("How many people to split the bill amount : "))

(bill_with_tip)= tip/100*bill + bill
print(f"Bill Before spliting: {bill_with_tip}")
split=bill_with_tip/people
print(f"Total bill after spliting for each person: {round(split,2)}")
