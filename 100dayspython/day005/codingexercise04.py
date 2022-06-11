print("FizzBuzz")
for number in range(1, 101):
    if number % 3 != 0 and number % 5 != 0 and number % 3 and 5 != 0:
        print(number)
    elif number % 3 == 0 and number % 5 != 0 and (number % 3 == number % 5) == 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0 and (number % 3 == number % 5) == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
