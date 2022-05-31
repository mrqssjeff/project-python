print('Welcome to the Tip Calculator!')
bill = float(input('What was the total bill? $'))
tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to splt the bill with?: '))
tip10 = bill * 0.1
bill10 = bill * 1.1
tip12 = bill * 0.12
bill12 = bill * 1.12
tip15 = bill * 0.15
bill15 = bill * 1.15
if tip == 10:
    print(f"""The tip is ${tip10:.2f}.
The bill plus the tip will be ${bill10:.2f}.
Each person should pay: ${bill10 / people:.2f}""")
elif tip == 12:
    print(f"""The tip is ${tip12:.2f}.
The bill plus the tip will be ${bill12:.2f}.
Each person should pay: ${bill12 / people:.2f}""")
elif tip == 15:
    print(f"""The tip is ${tip15:.2f}.
The bill plus the tip will be ${bill15:.2f}.
Each person should pay: ${bill15 / people:.2f}""")
