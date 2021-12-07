name = "VanyaChatbot"
birth_date = 2021
print(f"Hello! My name is {name}")
print(f"I was created in {birth_date}")
print("Please, remind me your name")
your_name = input()
print(f"What a great name you have {your_name}")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
i = 0
for i in range(number + 1):
    print(f"{i}!")
    i += 1

