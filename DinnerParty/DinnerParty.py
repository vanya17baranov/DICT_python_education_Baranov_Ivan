import random
print("Enter the number of friends joining (including you):")
number_of_friends = int(input(">"))
if number_of_friends <= 0:
    print("No one is joining for the party")

print("Enter the name of every friend (including you), each on a new line:")
names = {}
for i in range(number_of_friends):
    input_names = input(">")
    names[input_names] = 0

print("Enter the total amount")
money = int(input(">"))
for_all = round(money / number_of_friends, 2)
for i in names:
    names[i] = for_all
print(names)
print("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
choose = input(">")
if choose == "Yes":
    lucky_name = random.choice(list(names.keys()))
    print("{} is the lucky one!".format(lucky_name))
if choose == "No":
    print("No one is going to be lucky.")