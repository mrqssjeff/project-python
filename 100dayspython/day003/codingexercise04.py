print("Welcome to Python Pizza Deliveries!")
size = str(input("What size of pizza do you want? S, M or L: "))
add_pepperoni = str(input("Do you want pepperoni? Y or N:  "))
extra_cheese = str(input("Do you want extra cheese? Y or N: "))
bill = 0
small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_ml = 3
cheesy_pizza = 1
if size == "S":
    bill += small
    if add_pepperoni == "Y":
        bill += pepperoni_small
    if extra_cheese == "Y":
        bill += cheesy_pizza
    print(f"Your final bill is: ${bill:.2f}")
elif size == "M":
    bill += medium
    if add_pepperoni == "Y":
        bill += pepperoni_ml
    if extra_cheese == "Y":
        bill += cheesy_pizza
    print(f"Your final bill is: ${bill:.2f}")
elif size == "L":
    bill += large
    if add_pepperoni == "Y":
        bill += pepperoni_ml
    if extra_cheese == "Y":
        bill += cheesy_pizza
    print(f"Your final bill is: ${bill:.2f}")
