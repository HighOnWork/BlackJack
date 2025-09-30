import random

def value(cards_user, cards_computer):
    total = 0
    total_c = 0
    for card in cards_user:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            total += 11
        else:
            total += int(card)
    for card in cards_computer:
        if card in ['J', 'Q', 'K']:
            total_c += 10
        elif card == 'A':
            total_c += 11
        else:
            total_c += int(card)
    print("Total value of your cards is:", total)
    print("Computer's first card is:", cards_computer[0])
    if total > 21:
        print("You went over. You lose")
    elif total == 21:
        print("Blackjack! You win!")
    else:
        next_step(total, total_c, cards_computer, cards_user)

def blackJack():
    Cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    user_cards = []
    for i in range(2):
        user_cards.append(random.choice(Cards))
    print("Your cards are:", str(user_cards).replace("'", ""))
    computer_cards = []
    for i in range(2, 4):
        computer_cards.append(random.choice(Cards))
    value(user_cards, computer_cards)
    


def next_step(total, total_c, computer_cards, user_cards):
    choices = 0
    a_changed = False
    if choices < 1:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
        if choice == 'n':
            print("Computer's cards are:", str(computer_cards).replace("'", ""))
            print("Total value of computer's cards is:", total_c)
            if total_c > 21:
                if 'A' in computer_cards and not a_changed:
                    a_changed = True
                    total_c -= 10
                    next_step(total, total_c, computer_cards, user_cards)
                if 'A' in user_cards and not a_changed:
                    a_changed = True
                    total -= 10
                    print("Total value of your cards is:", total)
                    next_step(total, total_c, computer_cards, user_cards)
                print("Computer went over. You win!")
            elif total > total_c:
                print("You win!")
            elif total < total_c:
                print("You lose")
            else:
                print("It's a draw")
        elif choice == 'y':
            choices += 1
            Cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            user_cards.append(random.choice(Cards))
            print("Your cards are:", str(user_cards).replace("'", ""))
            value(user_cards, computer_cards)
    else:
        return


start = input("Do you want to start the program? (yes/no): ").strip().lower()
if start == 'yes':
    blackJack()
    