import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
comp_cards = []


def deal() -> int:
    return random.choice(cards)

def start_game():
    player_cards.clear()
    player_cards.append(deal())
    player_cards.append(deal())

    comp_cards.clear()
    comp_cards.append(deal())
    comp_cards.append(deal())


def play_game() -> bool:
    user_total = check_cards(player_cards)
    print("U:", player_cards, user_total)

    check_cards(comp_cards)
    comp_total = check_cards(comp_cards)
    print("C:", comp_cards, comp_total)

    if comp_total == 21:
        print("Computer wins")
        return False

    if user_total == 21:
        print("You win!!!")
        return False

    return True


def check_cards(c: []) -> int:
    total = 0
    for card in c:
        total += card

    return total

start_game()
while play_game():
    i = input("Deal a card? (y/n): ").lower()
    if i == "y":
        player_cards.append(deal())
        print(player_cards)
    else:
        user_total = check_cards(player_cards)
        comp_total = check_cards(comp_cards)
        if user_total > comp_total:
            print("You win!!!")
            break
        else:
            print("Computer wins")
            break

