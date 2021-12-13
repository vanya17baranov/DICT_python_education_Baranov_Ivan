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
    guesses.append(guess)
    attempts -= 1
    if guess not in answers:
        print("That letter doesn\'t appear in the word")
        if attempts == 0:
            break
    done = True
    for letter in answers:
        if letter not in guesses:
            done = False
print("Thanks for playing!")
print("We\'ll see how well you did in the next stage")
