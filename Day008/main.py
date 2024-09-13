
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[-(26-shift+1)])