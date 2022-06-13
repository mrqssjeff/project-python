print("Days in month!")


def is_leap(years):
    if years % 4 != 0 or years % 4 == 0 and years % 100 == 0 and years % 400 != 0:
        return False
    elif years % 4 == 0 and years % 100 != 0 or years % 4 == 0 and years % 100 == 0 and years % 400 == 0:
        return True


def days_in_month(years, months):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
    if months > 12 or months < -1:
        return "ERROR"
    elif is_leap(years) and months == 2:
        return month_days[-1]
    elif not is_leap(year):
        return month_days[months-1]



year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"The {month}th(nd) month in the year {year} has {days} days.")
