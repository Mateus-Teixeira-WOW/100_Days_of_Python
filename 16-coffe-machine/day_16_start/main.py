# from turtle import *
#
# timmy = Turtle()
# screen1 = Screen()
#
# print(timmy)
# timmy.shape("turtle")
#
# print(screen1.canvheight)
#
# timmy.forward(100)
#
# screen1.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Eletric"])
print(table)
table.align = "l"
print(table)