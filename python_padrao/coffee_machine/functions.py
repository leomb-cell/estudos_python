class Coffee:

    # constructor
    def __init__(self, water = 500.00, milk = 500.00, coffee = 500.00, money= 10.00):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cash_stock = money
        self.stock = {
            'water': water,
            'milk': milk,
            'coffee': coffee,
            'cinnamon': 300
        }
        self.blends = {         
            'latte': {
                'milk': 100,
                'water': 110,
                'coffee': 50,
            },            
            'expresso': {
                'milk': 0,
                'water': 250,
                'coffee': 150,
            },
            'cappuccino': {
                'milk': 200,
                'water': 160,
                'coffee': 90,
                'cinnamon': 5.00
            },
        }       
        self.menu = {
            'latte': 10.00,            
            'expresso': 15.00,
            'cappuccino': 18.00
        }

    # making coffee
    def makeCoffee(self, drink_type):
        # local variables 
        tem_tudo = True;
        blend = self.blends.get(drink_type.lower(), None)
        
        # cheking if valid blend
        if not blend:
            print("Invalid drink type!")
            return False

        # getting money
        while True:
            try:
                pay = float(input(f"The price will be {self.menu[drink_type]:.2f}:  \n"))
                break
            except ValueError:
                print("Invalid value!")
                continue

        # adding payment
        paid, change = self.pay(drink_type, pay)

        # checking if paid
        if not paid:
            return False        

        print("Alocating resources...")

        # checking resources 
        for name, qtd in blend.items():
            if not self.checkResource(name, qtd):
                tem_tudo = False
                print(f"{name} - not enough!")
            else:
                print(f"{name} - ok")

        if not tem_tudo: 
            print(f"Not enough ingredients to make {drink_type}")
            return False

        # taking resources
        for name, qtd in blend.items():
            self.takeResources(name, qtd)

        print(f"Take your {drink_type}, and here is your change {change:.2f}")

    # add resources
    def addResources(self, name, qtd):
        try:
            if qtd <= 0:
                raise ValueError("Zero or negative amount isn't allowed!")
            self.stock[name] += qtd
        except ValueError as error:
            print(f"Error: {error}")

    # take resources
    def takeResources(self, name, qtd):
        try:
            if qtd <= 0:
                raise ValueError("Zero or negative amount isn't allowed!")
            self.stock[name] -= qtd
        except ValueError as error:
            print(f"Error: {error}")
            return False

        return True

    # check resources
    def checkResource(self, name, qtd):    
        try:
            if (self.stock[name] - qtd) <= 0:
                return False
            else: 
                return True
        except ValueError as error:
            print(f"Error: {error}")

    # show resources
    def showResource(self):
        for name, qtd in self.stock.items():
            print(f"{name}: {qtd:.2f} un's") 
        print(f"balance: {self.cash_stock:.2f}")
        return True
        
    # payment and returning change
    def pay(self, name, qtd):
        price = self.menu[name]
        if qtd >= price:
            change = qtd - price

            self.cash_stock += self.menu[name]
            return True, change
        else:
            print("Not enough money...")
            return False, qtd
        
