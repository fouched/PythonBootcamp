from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password: str = ""

for i in range(0, nr_letters):
    rl= randint(0, len(letters)-1)
    password = password + letters[rl]

for i in range(0, nr_symbols):
    rs = randint(0, len(symbols)-1)
    password = password + symbols[rs]

for i in range(0, nr_numbers):
    rn = randint(0, len(numbers)-1)
    password = password + numbers[rn]

print(password)


# hard version mix up chosen characters
shuffled_password: str = ""
while True:
    if len(password) == 0:
        break

    r = randint(0, len(password)-1) + 1
    if r > 0 and len(password) > 1:
        char = password[r-1:r]
        shuffled_password += char
        password = password.replace(char, "", 1)
    else:
        shuffled_password += password
        break

print(shuffled_password)




