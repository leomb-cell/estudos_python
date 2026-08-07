import art
import functions

# variables

coffee = functions.Coffee()

while True:
    option = str(input("What would you like? (expresso/latte/cappuccino):   ")).lower()
    if option in ['expresso', 'latte', 'cappuccino']:
        coffee.makeCoffee(option)
    else:
        if option == 'off':
            print("Turning coffee machine off...")
            break
        else:
            if option == 'resources':
                coffee.showResource()