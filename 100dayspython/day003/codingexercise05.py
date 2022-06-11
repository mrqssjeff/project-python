print("Welcome to the Love Calculator!")
name1 = str(input("What is your name?: ")).strip().lower()
name2 = str(input("What is the others person name?: ")).strip().lower()
letter_t = name1.count("t") + name2.count("t")
letter_r = name1.count("r") + name2.count("r")
letter_u = name1.count("u") + name2.count("u")
letter_e = name1.count("e") + name2.count("e")
letter_l = name1.count("l") + name2.count("l")
letter_o = name1.count("o") + name2.count("o")
letter_v = name1.count("v") + name2.count("v")
true = str(letter_t + letter_r + letter_u + letter_e)
love = str(letter_l + letter_o + letter_v + letter_e)
true_love = true + love
score = int(true_love)
if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
