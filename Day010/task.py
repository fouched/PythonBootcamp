# def format_name(f_name: str, l_name: str) -> str:
#     return f"{f_name.title()} {l_name.title()}"
#
# full_name = format_name("anGelA", "YU")
# print(full_name)

# def is_leap_year(year: int) -> bool:
#     """
#         Returns True is year is a leap year,False if not
#     """
#     if year % 4 == 0:
#         if year % 100 == 0:
#             return False
#         elif year % 400 == 0:
#             return False
#
#         return True
#     else:
#         return False
#
#
# y = input("Enter year:\n")
#
# if is_leap_year(int(y)):
#     print(f"{y} is a leap year")
# else:
#     print(f"{y} is not a leap year")

def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)