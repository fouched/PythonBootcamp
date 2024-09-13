
# def greet(name: str):
#     print(f"Hello {name}")
#
#
# greet("Fouche")
#
# def life_in_weeks(current_age: int):
#     weeks = (90 - current_age) * 52
#     print(f"You have {weeks} weeks left.")
#
#
# life_in_weeks(52)


# def greet_with(name: str, location: str):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")
#
#
# greet_with("Fouche", "Cape Town")
#
# greet_with(location="Port Elizabeth", name="John")


def calculate_love_score(name1: str, name2: str):

    t_word = "TRUE"
    l_word = "LOVE"

    combined_name = name1 + name2
    count1 = 0
    count2 = 0

    for letter in combined_name.upper():
        if letter in t_word:
            count1 += 1

    for letter in combined_name.upper():
        if letter in l_word:
            count2 += 1

    print(f"{count1}{count2}")


calculate_love_score("Angela Yu", "Jack Bauer")