
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(word: str, s: int):
    if s > 26:
        print("You cannot shift by more than 26")
        return

    encrypted = ""
    for letter in word:
        if letter == " ":
            encrypted += " "
        else:
            idx = alphabet.index(letter)
            print(f"Idx: {idx}")
            encrypted += alphabet[-(26-shift-idx)]

    print(f"Encrypted: {encrypted}")


encrypt(text, shift)
