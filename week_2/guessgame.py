''' Word guessing game '''
import random

#list of 20 preset words
words = ["endure", "cheese", "impair", "decision", "empty", "cream", "five", \
         "cat", "dolls", "comb", "sassy", "story", "hopitable", "joyous", \
         "minor", "connection", "respect", "xylophone", "zebra", "hoax"]
secret = ""
guesses = None
mode = None


def generate_random(dif):
    global guesses
    if dif == 1:
        guesses = 11
    elif dif == 2:
        guesses = 9
    elif dif == 3:
        guesses = 7
    elif dif == 4:
        guesses = 5
    elif dif == 5:
        guesses = 3
    else:
        guesses = None


def init():
    global secret, words, mode
    x = random.randint(0, 19)
    secret = words[x]
    mode = input("Please enter 1 to play guessing game, 2 to play hangman")


def guess():
    global secret, guesses
    isRunning = True
    msg = ""

    #set difficulty
    while guesses == None:
        dif = input("What difficulty would you like to play on? 1 - 5: ")
        if (str.isdigit(dif)):
            # setup guess count and secret number
            generate_random(int(dif))
        else:
            print("Please note, only numbers allowed.")
        if guesses == None and str.isdigit(dif):
            print("Please use a valid difficulty!")

    #run game
    guess = None
    while isRunning:
        msg = ""
        guess = input("Guess the word: ")
        guesses -= 1
        if guess == secret:
            msg += "Congratulations, Ypu've guessed correctly\n"
            guesses = 0
        else:
            msg += "Incorrect!\n"

        if guesses == 0:
            msg += "GAME OVER!"
            isRunning = False
        else:
            msg += "Try again!"
        print(msg)


''' Main function to run '''
def main():
    global mode, secret
    game = True
    while game:
        init()
        if mode == "1":
            print(F"For testing, the word is: {secret}")
            guess()
            game = False
        elif mode == "2":
            #hang()
            game = False
        else:
            print("Please enter either 1 or 2")



if __name__ == '__main__':
    main()
