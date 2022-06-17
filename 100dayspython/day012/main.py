import random
comp_number = random.randint(1, 100)


def difficulty_level(levels):
    if levels == 'easy':
        return 10
    elif levels == 'hard':
        return 5


def player_guesses(player_guess):
    if player_guess > comp_number:
        return f"Too high.\nGuess Again.\n"\
               f"You have {attempts} attempts remaining to guess the number."
    elif player_guess < comp_number:
        return f"Too Low. \nGuess Again.\n"\
               f"You have {attempts} attempts remaining to guess the number."
    elif player_guess == comp_number:
        return f"YOU WIN! The answer was {comp_number}."


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).strip().lower()
attempts = difficulty_level(difficulty)
print(f"You have {difficulty_level(difficulty)} attempts remaining to guess the number.")
for counting in range(attempts):
    guess = int(input("Make a guess: "))
    print(player_guesses(guess))
    if guess == comp_number:
        break
    attempts -= 1
