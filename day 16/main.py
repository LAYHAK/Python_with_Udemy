# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("circle")
# timmy.color("black", "green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Country", ["India", "China", "USA", "Indonesia"])
table.add_column("Rank", [1, 2, 3, 0])

table.align["Country"] = "l"
print(table)
