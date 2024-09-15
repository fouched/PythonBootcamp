
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(word: str, s: int):
    encrypted = ""
    for letter in word:
        if letter == " ":
            encrypted += " "
        else:
            idx = alphabet.index(letter)
            encrypted += alphabet[-(26-shift-idx)]

    print(f"Encrypted: {encrypted}")


def decrypt(word: str, s: int):
    decrypted = ""
    for letter in word:
        if letter == " ":
            decrypted += " "
        else:
            idx = alphabet.index(letter)
            decrypted += alphabet[idx - shift]

    print(f"Decrypted: {decrypted}")

if shift > 26:
    print("You cannot shift by more than 26")
else:
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input")
