def odd_or_even(value):
    if value % 2 == 0:
        return "This is an even number!"
    else:
        return "This is an odd number!"


number = int(input("Which number do you want to check?: "))
print(odd_or_even(number))
