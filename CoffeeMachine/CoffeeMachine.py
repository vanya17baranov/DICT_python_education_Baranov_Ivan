class CoffeeMachine:

    def __init__(self):
        self.water_amount = 400
        self.milk_amount = 540
        self.beans_amount = 120
        self.money_amount = 550
        self.cups_amount = 9

    def amount(self):
        print(f"""The coffee machine has:
        {self.water_amount} of water
        {self.milk_amount} of milk
        {self.beans_amount} of coffee beans
        {self.cups_amount} of disposable cups
        {self.money_amount} of money""")

    def money(self):
        print(f"I gave you {self.money_amount}")
        self.money_amount = 0
        print("")
        print(f"""The coffee machine has:
              {self.water_amount} of water
              {self.milk_amount} of milk
              {self.beans_amount} of coffee beans
              {self.cups_amount} of disposable cups
              {self.money_amount} of money""")

    def add(self):
        self.water_amount = self.water_amount + int(input("Write how many ml of water you want to add:"))
        self.milk_amount = self.milk_amount + int(input("Write how many ml of milk you want to add:"))
        self.beans_amount = self.beans_amount + int(input("Write how many grams of coffee beans you want to add:"))
        self.cups_amount = self.cups_amount + int(input("Write how many disposable coffee cups you want to add:"))
        print(f"""The coffee machine has:
              {self.water_amount} of water
              {self.milk_amount} of milk
              {self.beans_amount} of coffee beans
              {self.cups_amount} of disposable cups
              {self.money_amount} of money""")

    def coffee(self):
        coffee_types = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if coffee_types == "1":
            self.water_amount -= 250
            self.beans_amount -= 16
            self.money_amount += 4
            self.cups_amount -= 1
            print("Making your coffee")
            print(f"""The coffee machine has:
              {self.water_amount} of water
              {self.milk_amount} of milk
              {self.beans_amount} of coffee beans
              {self.cups_amount} of disposable cups
              {self.money_amount} of money""")
        elif coffee_types == '2':
            self.water_amount -= 350
            self.milk_amount -= 75
            self.beans_amount -= 20
            self.money_amount += 7
            self.cups_amount -= 1
            print("Making your coffee")
            print(f"""The coffee machine has:
              {self.water_amount} of water
              {self.milk_amount} of milk
              {self.beans_amount} of coffee beans
              {self.cups_amount} of disposable cups
              {self.money_amount} of money""")
        elif coffee_types == "3":
            self.water_amount -= 200
            self.milk_amount -= 100
            self.beans_amount -= 12
            self.money_amount += 6
            self.cups_amount -= 1
            print("Making your coffee")
            print(f"""The coffee machine has:
              {self.water_amount} of water
              {self.milk_amount} of milk
              {self.beans_amount} of coffee beans
              {self.cups_amount} of disposable cups
              {self.money_amount} of money""")


defs = CoffeeMachine()


def menu():
    choose = input('Write action (buy, fill, take):')
    if choose == 'buy':
        defs.coffee()
    elif choose == 'take':
        defs.money()
    elif choose == 'fill':
        defs.add()


menu()
