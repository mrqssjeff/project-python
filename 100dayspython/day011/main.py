import random

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    add = sum(card_list)
    if add == 21:
        return 0
    elif add > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return add
    else:
        return add


def compare(user, pc):
    if user == pc:
        return "It's a draw!"
    elif user == 0:
        return "Blackjack! YOU WIN!"
    elif user > 21:
        return "You're over 21. YOU LOST."
    elif pc == 0:
        return "YOU LOSE. Computer has a Blackjack!"
    elif pc > 21:
        return "Computer is over 21. YOU WIN!"
    elif user > pc:
        return "YOU WIN! You have the highest score!"
    elif pc > user:
        return "YOU LOSE. Computer has the highest score!"


computer = []
player = []
while True:
    computer.clear()
    player.clear()
    game = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).strip().lower()
    if game == 'n':
        break
    p_first_hand = deal_card(), deal_card()
    c_first_hand = deal_card(), deal_card()
    player.extend(p_first_hand)
    computer.extend(c_first_hand)
    player_score = calculate_score(player)
    computer_score = calculate_score(computer)
    print(f"Your cards: {player}")
    print(f"Computer's first card: {computer[0]}")
    if player_score == 0:
        print("Blackjack! YOU WIN!")
        break
    elif computer_score == 0:
        print(f"Computer's hand is {computer}")
        print("YOU LOSE! Computer has a Blackjack!")
        break
    new_card = str(input("Type 'y' to get a new card or type 'n' to pass: "))
    if new_card == 'y':
        player.append(deal_card())
        player_score = calculate_score(player)
        print(f"Your new card is {player[-1]}")
        if computer_score < 16:
            computer.append(deal_card())
            computer_score = calculate_score(computer)
            print(f"Computer's new card is {computer[-1]}")
            if player_score > 21 or player_score == 0 or computer_score > 21 or computer_score == 0:
                print(f"Your hand is {player}")
                print(f"Computer's hand is {computer}")
                print(compare(player_score, computer_score))
                break
        else:
            print(f"Your hand is {player}")
            print(f"Computer's hand is {computer}")
            print(compare(player_score, computer_score))
            break
    elif new_card == 'n':
        print(f"Your hand is {player}")
        print(f"Computer's hand is {computer}")
        print(compare(player_score, computer_score))
        break
