import random
print("HANGMAN")
print("The game will be available soon")
words = ["java", "javascript", "python", "php"]
answers = random.choice(words)
help = answers[0] + answers[1] + answers[2] + "-" * (len(answers) -3)
print("Guess the word " + help + ":")
answer = input()
if answer == answers:
    print("You survived!")
else:
    print("You lost!")
