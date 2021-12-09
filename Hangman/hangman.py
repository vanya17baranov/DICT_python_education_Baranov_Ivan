import random
print("HANGMAN")
print("The game will be available soon")
words = ["java", "javascript", "python", "php"]
answers = random.choice(words)
print("Guess the word:")
answer = input()
if answer == answers:
    print("You survived!")
else:
    print("You lost!")
