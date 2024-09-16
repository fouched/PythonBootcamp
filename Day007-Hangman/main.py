import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6

# chosen_word = word_list[randint(0, len(word_list)-1)]
# easier than above
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

word_guessed = False
correct_letters = []

while not word_guessed:
    guess = input("Choose a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1

    print(lives)
    print(stages[lives])
    print(display)

    if "_" not in display:
        word_guessed = True
        print("You win.")
        break

    if lives == 0:
        print("You loose")
        break


