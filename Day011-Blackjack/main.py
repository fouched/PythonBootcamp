import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
comp_cards = []


def deal() -> int:
    return random.choice(cards)

def start_game() -> bool:
    player_cards.clear()
    player_cards.append(deal())
    player_cards.append(deal())
    print("P:", player_cards)

    comp_cards.clear()
    comp_cards.append(deal())
    comp_cards.append(deal())
    print("C:", comp_cards[0])

    if check_total(comp_cards) == 21:
        return False
    else:
        return True


def check_total(c: []) -> int:
    total = 0
    for card in c:
        total += card

    return total


def player_turn() -> bool:
    i = input("Deal a card? (y/n): ").lower()
    if i == "y":
        card = deal()
        player_cards.append(card)
        return True
    else:
        return False


def computer_turn() -> bool:
    comp_total = check_total(comp_cards)
    if comp_total < 17:
        card = deal()
        comp_cards.append(card)
        return True
    else:
        return False

def print_final_score():
    computer_total = check_total(comp_cards)
    player_total = check_total(player_cards)

    print("")
    print("==============================")
    print("Player cards:", player_cards)
    print("Computer cards:", comp_cards)
    print(f"Final score: P:{player_total} C:{computer_total}")
    print("==============================")

    if player_total > 21:
        print("Computer wins :-(")
    elif computer_total > 21:
        print("You win!!!")
    elif player_total == computer_total:
        print("Draw")
    elif player_total > computer_total:
        print("You win!!!")
    else:
        print("Computer wins :-(")

    print("==============================")


def play_game():
    cont_game = start_game()

    if cont_game:
        while player_turn():
            print("Player:", player_cards)
            if check_total(player_cards) > 21:
                print("You bust!")
                break

        if check_total(player_cards) <= 21:
            while computer_turn():
                print("Computer:", comp_cards)
                if check_total(comp_cards) > 21:
                    print("Computer bust!")
                    break

    print_final_score()

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        print("\n" * 20)
        play_game()
    else:
        print("Goodbye!")


play_game()




