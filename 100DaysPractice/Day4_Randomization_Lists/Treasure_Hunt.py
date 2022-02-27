print("Welcome for Treasure hunt")
row1=["_","_","_"]
row2=["_","_","_"]
row3=["_","_","_"]
map=[row1,row2,row3]
print(f"{row1} \n{row2} \n{row3}")
position=input("Enter the row and column where would you like to place treasure? :" )

# Divide the string by spliting

Horizontal=int(position[0])
Vertical=int(position[1])

# map=[[Vertical-1][Horizontal-1]]= "X"
selected_row=map[Vertical-1]
selected_row[Horizontal-1]="X"
print(f"{row1} \n{row2} \n{row3}")