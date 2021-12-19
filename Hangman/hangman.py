import random
print("HANGMAN")
def main():
    attempts = 8
    words = ["java", "javascript", "python", "php"]
    answers = random.choice(words)
    guesses = []
    done = False
    incorrect_guesses = []
    while not done:
        for letter in answers:
            if letter in guesses:
                print(letter, end='')
            else:
                print("_", end="")
        print("")
        guess = input("Input a letter:")
        if len(guess) != 1:
            print("You should input a single letter.")
        elif guess.isupper() is True:
            print("Please enter a lowercase English letter.")
        elif guess in incorrect_guesses:
            print("You\'ve already guessed this letter.")
        elif guess not in answers:
            attempts -= 1
            incorrect_guesses.append(guess)
            print("That letter doesn\'t appear in the word")
        elif guess in guesses:
            print("You\'ve already guessed this letter.")
        else:
            guesses.append(guess)
            if attempts == 0:
                break
            done = True
            for letter in answers:
                if letter not in guesses:
                    print(1)
                    done = False
        if done:
            print("You guessed the word {}!".format(answers))
            print("You survived!")
        else:
            print("You lost!")
            print(done)
main()