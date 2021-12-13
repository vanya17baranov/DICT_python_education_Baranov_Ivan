import random
print("HANGMAN")
print("The game will be available soon")
attempts = 8
words = ["java", "javascript", "python", "php"]
answers = random.choice(words)
guesses = []
done = False
while not done:
    for letter in answers:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("")
    guess = input("Input a letter:")
    if guess in guesses:
        attempts -= 1
        print('No improvements')
    if guess in answers:
        guesses.append(guess)
    else:
        attempts -= 1
    print("That letter doesn\'t appear in the word")
    if attempts == 0:
        break
    done = True
    for letter in answers:
        if letter not in guesses:
            done = False
if done:
    print('Congrats')
else:
    print('Game over')
