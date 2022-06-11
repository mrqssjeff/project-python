def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
