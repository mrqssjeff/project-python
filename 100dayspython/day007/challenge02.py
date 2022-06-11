import random
word_list = ["brazil", "denmark", "china", "finland", "mexico"]
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display += "_"
guess = str(input("A word was assigned! Guess a letter: ")).strip().lower()
for position, letter in enumerate(chosen_word):
    if letter == guess:
        display[position] = letter
print(display)
print(f"The assigned word was: {chosen_word}")
