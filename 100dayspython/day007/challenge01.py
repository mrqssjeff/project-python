import random
word_list = ["brazil", "denmark", "china", "finland", "mexico"]
chosen_word = random.choice(word_list)
guess = str(input("A word was assigned! Guess a letter: ")).strip().lower()
for letter in chosen_word:
    if letter == guess:
        print("Right!")
    elif letter != guess:
        print("Wrong!")
print(f"The assigned word was: {chosen_word}")
