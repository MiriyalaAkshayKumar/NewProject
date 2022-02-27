# 155 175 165 177 180 164 185 157 158
print("Calculating Highest Score")
student_score = input("Enter the score for each student : ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
print(max(student_score))

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"This is the highest score: {highest_score}")
