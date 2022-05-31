print("Leap Year!")
year = int(input("Which year do you want to check?: "))
leap = True
if year % 4 != 0:
    leap = False
elif year % 4 == 0 and year % 100 != 0:
    leap = True
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    leap = False
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    leap = True

print(f"The year {year} is a leap year: {leap}")
