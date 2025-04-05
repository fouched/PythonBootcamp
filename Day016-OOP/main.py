# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

tbl = PrettyTable()
tbl.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
tbl.add_column("Type", ["Electric", "Water", "Fire"])
tbl.align = "l"

print(tbl)