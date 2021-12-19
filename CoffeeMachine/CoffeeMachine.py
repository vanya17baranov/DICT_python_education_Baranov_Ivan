class CoffeeMachine:

    def __init__(self):
        self.water_amount = 400
        self.milk_amount = 540
        self.beans_amount = 120
        self.money_amount = 550
        self.cups_amount = 9

    def remaining(self):
        print(f"""The coffee machine has:
        {self.water_amount} of water
        {self.milk_amount} of milk
        {self.beans_amount} of coffee beans
        {self.cups_amount} of disposable cups
        {self.money_amount} of money""")

    def money(self):
        print(f"I gave you {self.money_amount}")
        self.money_amount = 0

    def add(self):
        self.water_amount = self.water_amount + int(input("Write how many ml of water you want to add:"))
        self.milk_amount = self.milk_amount + int(input("Write how many ml of milk you want to add:"))
        self.beans_amount = self.beans_amount + int(input("Write how many grams of coffee beans you want to add:"))
        self.cups_amount = self.cups_amount + int(input("Write how many disposable coffee cups you want to add:"))

    def espresso(self):
        if self.water_amount < 250:
            print("Sorry, not enough water!")
        elif self.beans_amount < 16:
            print("Sorry, not enough beans!")
        elif self.cups_amount < 1:
            print("Sorry, not enough cups!")
        else:
            self.water_amount -= 250
            self.beans_amount -= 16
            self.cups_amount -= 1
            self.money_amount += 4
            print("I have enough resources, making you a coffee!")
        print("")

    def latte(self):
        if self.water_amount < 350:
            print("Sorry, not enough water!")
        elif self.beans_amount < 20:
            print("Sorry, not enough beans!")
        elif self.cups_amount < 1:
            print("Sorry, not enough cups!")
        elif self.milk_amount < 75:
            print("Sorry not enough milk!")
        else:
            self.water_amount -= 350
            self.beans_amount -= 20
            self.cups_amount -= 1
            self.milk_amount -= 75
            self.money_amount += 7
            print("I have enough resources, making you a coffee!")
        print("")

    def cappuccino(self):
        if self.water_amount < 200:
            print("Sorry, not enough water!")
        elif self.beans_amount < 12:
            print("Sorry, not enough beans!")
        elif self.cups_amount < 1:
            print("Sorry, not enough cups!")
        elif self.milk_amount < 100:
            print("Sorry not enough milk!")
        else:
            self.water_amount -= 200
            self.beans_amount -= 12
            self.cups_amount -= 1
            self.milk_amount -= 100
            self.money_amount += 6
            print("I have enough resources, making you a coffee!")
        print("")


defs = CoffeeMachine()


def coffee():
    choose = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    if choose == '1':
        defs.espresso()
    elif choose == '2':
        defs.latte()
    elif choose == '3':
        defs.cappuccino()
    elif choose == 'back':
        menu()


def menu():
    while True:
        choose = input("Write action (buy, fill, take, remaining, exit):")
        if choose == "buy":
            coffee()
        elif choose == "take":
            defs.money()
        elif choose == "fill":
            defs.add()
        elif choose == "remaining":
            defs.remaining()
        elif choose == "exit":
            break


menu()
