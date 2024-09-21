import random


EASY = 10
HARD = 5

def make_guess(guesses_remaining, answer_num) -> int:
    print(f"You have {guesses_remaining} remaining to guess the number.")
    guess_num = int(input("Make a guess: "))

    if guess_num == answer_num:
        return guess_num
    elif guess_num < answer_num:
        print("Too low")
        return 0
    else:
        print("Too high")
        return 0

def set_level() -> int:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY
    else:
        return HARD

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num_guesses = set_level()
    answer_num = random.randint(1, 100)

    while num_guesses > 0:
        answer = make_guess(num_guesses, answer_num)
        if answer >= 1:
            print(f"Correct, the number was {answer}, well done!")
            break
        else:
            num_guesses -= 1

        if num_guesses == 0:
            print("You loose")
            break
        else:
            print("Guess again")


play_game()

