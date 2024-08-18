import random


def card_deal():
    """Returns a random card from deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card= random.choice(cards)
    return card


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Loss , opponent has Blackjack 😫"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif c_score > 21:
        return "opponent went over. You win 😁"
    elif u_score>21:
        return "You went over, You lose 😕"
    elif u_score > c_score:
        return "You win 🙂"
    else:
        return "You lose 😤"


def play_game():
    user_card = []
    computer_card=[]
    user_score= -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(card_deal())
        computer_card.append(card_deal())

    def calculate_score(card_score):
        if sum(card_score)==21 and len(card_score) ==2:
            return 0
        if 11 in card_score and sum(card_score)>21:
            card_score.remove(11)
            card_score.append(1)

        return sum(card_score)

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your Cards:{user_card}\nYour Current Score: {user_score}\n")
        print(f"Computer's First Card: {computer_card[0]}\n")

        if user_score == 0 or computer_score ==0 or user_score > 21:
            is_game_over= True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass:\n")
            if choice == 'y':
                user_card.append(card_deal())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score<17:
        computer_card.append(card_deal())
        computer_score = calculate_score(computer_card)

    print(f"Your Final hand: {user_card }\nFinal Score: {user_score}\n")
    print(f"Computer's Final Hand: {computer_card}\nFinal Score: {computer_score}\n")

    print(compare(u_score=user_score,c_score=computer_score))


while input("Do you want to play Blackjack? Type'y' or 'n':\n") == 'y':
    play_game()

