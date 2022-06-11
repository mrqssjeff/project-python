students_heights = input("Input a list of students heights: ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

count = plus = average = 0
for height in students_heights:
    plus += height
    count += 1
    average = round(plus / count)
print(f"The average height of the informed list is: {average}")



