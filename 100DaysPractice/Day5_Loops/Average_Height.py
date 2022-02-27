# 155 175 165 177 180 164 185 157 158
print("Calculating Average Height")
student_heights = input("Enter the heights for each student : ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height: {total_height}")

No_of_students=0
for students in student_heights:
    No_of_students+=1
print(f"No_of_students: {No_of_students}")

Average=total_height/No_of_students
print(f"Average is : {round(Average,2)}")