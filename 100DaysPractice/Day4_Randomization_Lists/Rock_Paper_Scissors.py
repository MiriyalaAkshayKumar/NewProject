import random

print("Welcome to rock ,paper and scissor game")
user_choice=int(input("Enter your user choice: "))
rock=0
paper=1
scissor=2
game=[rock,paper,scissor]


computer_choice=random.randint(0,2)

if user_choice >=3 or user_choice<0:
    print("Its Invalid")
else:
    print("Wait for computer choice")
    print(f"Computer choice is :{computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice ==0:
    print("you lose")
elif user_choice<computer_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You Win")
elif user_choice == computer_choice:
    print("You Draw")
else:
    print(game)