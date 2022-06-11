import random
word_list = ["brazil", "denmark", "china", "finland", "mexico"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display += "_"
print("A word was assigned!")
game_over = False
while not game_over:
    guess = str(input("Guess a letter: ")).strip().lower()
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        game_over = True
print(f"CONGRATULATIONS! YOU'VE WON! The assigned word was: {chosen_word}")
