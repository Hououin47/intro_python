# program to guess a secret number
# Tahir-mahmood Rhoda
# 14 february 2011
import random
# global variables:
guesses = None
secret = 0

'''generate random number between 0 and 50xdifficulty level, also give less guesses allowed as dif increases'''
def generate_random(dif):
    global guesses, secret
    if dif == 1:
        guesses = 20
        secret = random.randint(0, (dif*50))
    elif dif == 2:
        guesses = 15
    elif dif == 3:
        guesses = 10
    elif dif == 4:
        guesses = 5
    elif dif == 5:
        guesses = 1
    else:
        guesses = None
    secret  = random.randint(0, (dif*50))


''' This method sets up a dynamic message based on how faer off the guess is '''
def define_range(guess):
    global secret
    dif  = abs(secret - guess)

    msg = ""
    if dif <= 5:
        msg = "OOOOOH, So close, but a little too "
    elif dif <= 15:
        msg = "well, you're kinda close, but a bit too "
    elif dif <= 30:
        msg = "You're kinda far away, that's much too "
    elif dif <= 50:
        msg = "Damn! You're going to have to up your guessing game, That's way too "
    elif dif <= 100:
        msg = "Just give up. Really, thats just... just impossible to be that "
    else:
        msg = "This shouldn't happen"
    return msg

def run_game():
    global guesses, secret
    isRunning = True

    while isRunning:
        guess = None

        #check that guess is valid
        while guess == None:
            guess = input("What is the secret number? ")
            if not str.isdigit(guess):
                print("Please only enter numbers")
                guess = None
            else:
                guess = int(guess)
        guesses -= 1

        if guess == secret:
            msg = "Congratulations, you have guessed the secret number!"
            guesses = 0
        elif guess < secret:
            msg = define_range(guess) + "LOW.\n"
            if guesses > 0:
                msg += "Please try again."
            else:
                msg = "Game Over! You're outta guesses!"
        elif guess > secret:
            msg = define_range(guess) + "HIGH.\n"
            if guesses > 0:
                msg += "Please try again."
            else:
                msg = "Game Over! You're outta guesses!"
        else:
            msg = "This shouldnt happen\n"

        print(msg)
        guess = None
        #break out if out of guesses/ won
        if guesses == 0:
            isRunning = False


def main():
    while guesses == None:
        dif = input("What difficulty would you like to play on? 1 - 5: ")
        if (str.isdigit(dif)):
            # setup guess count and secret number
            generate_random(int(dif))
        else:
            print("Please note, only numbers allowed.")
        if guesses == None and str.isdigit(dif):
            print("Please use a valid difficulty!")
    run_game()


if __name__ == '__main__':
    main()
