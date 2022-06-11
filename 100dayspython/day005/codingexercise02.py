students_scores = input("Input a list of students scores: ").split()
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])

highest = count = 0
for score in students_scores:
    count += 1
    if count == 1:
        highest = score
    elif count > 1:
        if score > highest:
            highest = score

print(f"The highest score in the class is: {highest}")
