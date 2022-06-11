import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["brazil", "denmark", "china", "finland", "mexico"]
chosen_word = random.choice(word_list)
display = []
lives = 6
for letter in chosen_word:
    display += "_"
print("A word was assigned!")
end_game = False
while not end_game:
    guess = str(input("Guess a letter: ")).strip().lower()
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter
    if guess not in display:
        lives -= 1
    display_b = ''
    for character in display:
        display_b += f" {character}"
    while lives > 0:
        print(display_b)
        print(stages[lives])
        print(f"You still have {lives} lives!")
        break
    if lives == 0:
        print(display_b)
        print(stages[lives])
        print(f"YOU LOSE! The assigned word was: {chosen_word}")
        end_game = True
    if "_" not in display:
        print(display_b)
        print(stages[lives])
        print(f"CONGRATULATIONS! YOU'VE WON! The assigned word was: {chosen_word}")
        end_game = True
