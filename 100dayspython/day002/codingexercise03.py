print('Your life in weeks!!')
age = int(input('What is your current age?: '))
months = age * 12
weeks = age * 52
days = age * 365
print(f"You've already lived {months} months, {weeks} weeks, {days} days.")
print(f'And you have {(90 * 12) - months}, {(90 * 52) - weeks} and {(90 * 365) - days} days left.')
