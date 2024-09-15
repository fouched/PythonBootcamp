
# some_dict = {
#     "apple": "red",
#     "pear": "green",
#     "banana": "yellow",
# }
#
# print(some_dict["pear"])
#
# # add something
# some_dict["orange"] = "orange"
# # overwrite
# some_dict["apple"] = "red or green"
#
# print(some_dict)
#
# # loop
# for key in some_dict:
#     print(some_dict[key])
#
# # wipe
# some_dict = {}
#
# print(some_dict)

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_scores[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_scores[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70:
#         student_scores[key] = "Acceptable"
#     else:
#         student_scores[key] = "Fail"
#
# print(student_scores)

# nesting
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Frankfurt", "Stuttgart"],
}

print(travel_log["France"][1])

travel_log = {
    "France" : {
        "cities_visited":  ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited":  ["Berlin", "Frankfurt", "Stuttgart"],
        "total_visits": 8
    }
}

print(travel_log["Germany"]["cities_visited"][2])
