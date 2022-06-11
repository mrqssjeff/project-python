import random
print("Rock, Paper, Scissors!")
player = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors: "))
computer = random.randint(0, 2)
game = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

if player == 0:
    print(game[0])
elif player == 1:
    print(game[1])
elif player == 2:
    print(game[2])

if computer == 0:
    print("Computer chose:")
    print(game[0])
elif computer == 1:
    print("Computer chose:")
    print(game[1])
elif computer == 2:
    print("Computer chose:")
    print(game[2])

if player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
    print("YOU WIN!")
elif player == 0 and computer == 0 or player == 1 and computer == 1 or player == 2 and computer == 2:
    print("IT'S A TIE!")
if player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
    print("YOU LOSE!")
else:
    print("404! ERROR!")
    print("""
                                           \ / _
                                      ___,,,
                                      \_[o o]
     Invalid Number!                  C\  _\/
             /                     _____),_/__
        ________                  /     \/   /
      _|       .|                /      o   /
     | |       .|               /          /
      \|       .|              /          /
       |________|             /_        \/
       __|___|__             _//\        \
 _____|_________|____       \  \ \        \
                    _|       ///  \        \
                   |               \       /
                   |               /      /
                   |              /      /
 ________________  |             /__    /_
 bger        ...|_|.............. /______\.......""")
