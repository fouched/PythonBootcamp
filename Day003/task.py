
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are R 5")
    elif age <= 17:
        bill = 7
        print("Youth tickets are R 7")
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
        print("Adult tickets areR 12")

    add_photo = input("Do you want a photo ? (y / n)")
    if add_photo == "y":
        bill += 3

    print(f"You need to pay {bill}")
else:
    print("Too short")


# number = int(input("Enter number: "))
# result = number % 2
# if result == 0:
#     print("Even number")
# else:
#     print("Odd number")

# weight = 85
# height = 1.85
# bmi = weight / (height ** 2)
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi <= 25:
#     print("normal weight")
# else:
#     print("overweight")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M, L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y / N: ")
# extra_cheese = input("Do you want extra cheese? Y / N: ")

# S = 15, M = 20, L = 25
# Pepperoni S: 2, M/L: 3
# Extra cheese: 1

# bill = 0
# if size == "S":
#     bill += 15
#     if pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if pepperoni == "Y":
#         bill += 3
# else:
#     bill += 25
#     if pepperoni == "Y":
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill: {bill}")