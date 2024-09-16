import art

print(art.logo)
bids = {}
cont = "yes"

while cont == "yes":
    name = input("Enter your name:\n")
    bid = input("Bid:\n")
    bids[name] = bid
    cont = input("Continue?\n").lower()


print(bids)

name = ""
highest = 0
for key in bids:
    if int(bids[key]) > int(highest):
        name = key
        highest = bids[key]

print(f"Bid won by {name} with {highest}")

