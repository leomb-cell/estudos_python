# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

def clear_terminal_ansi():
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")

clear_terminal_ansi()

# creating object

table = PrettyTable()

# adding columns

table.add_column("Pokemon Name", ["pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])


#printing table

print(table)