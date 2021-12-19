water_amount = int(input("Write how many ml of water the coffee machine has:"))
milk_amount = int(input("Write how many ml of milk the coffee machine has:"))
beans_amount = int(input("Write how many grams of coffee beans the coffee machine has:"))
amount = int(input("Write how many cups of coffee you will need:"))
storage = [water_amount // 200, milk_amount // 50, beans_amount // 15]
if min(storage) > amount:
    print(f"Yes, I can make that amount of coffee (and even {min(storage) - amount} more than that)")
elif min(storage) == amount:
    print("Yes, I can make that amount of coffee")
elif min(storage) < amount:
    print(f"No, I can make only {min(storage)} cups of coffee")
print("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")
