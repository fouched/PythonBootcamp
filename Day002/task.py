# subscripting
# print("Hello"[4])
# print("Hello"[1:2])
# print("Hello"[:2])

# name = input("Enter your name:")
# name_len = len(name)
# print("Number of letters in your name:" + str(name_len))

# print(2 ** 3)
#
# height = 1.82
# weight = 85

# Write your code here.
# Calculate the bmi using weight and height.
# bmi = weight / (height**2)
#
# print(round(bmi,2))
#
# print(f"BMI {bmi}")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? R "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total = (bill * (tip/100)) + bill
split = round(total/people, 2)
print(f"Each person should pay: R {split}")