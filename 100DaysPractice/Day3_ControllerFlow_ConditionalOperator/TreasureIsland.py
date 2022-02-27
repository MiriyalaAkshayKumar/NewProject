print("Welcome to Treasure Island")
choice1 = input('Enter your choice 1 "Left" or "Right" : ')
if choice1 == "Left":
    choice2 = input('Enter your choice 2 "Wait" or "Swim" : ')
    if choice2 == "Wait":
        door = input('Enter the door colour "Red" , "Yellow" , "Blue"')
        if door == "Red":
            print("Game Over")
        elif door =="Yellow":
            print("You won the game")
        elif door == "Blue":
            print("Game Over")
        else:
            print("You chose the door doesn't exists")
    else:
        print("You have drown,Game over")
else:
    print("You have fell into hole, Game Over")