print("Calculating Even number from 1 to 100 using Range Method")

total=0
for number in range(2,101,2):
    #print(number)
    total+=number
print(total)

total2=0
for number in range(1,101):
    if number %2==0:
        total2+=number
print(total2)