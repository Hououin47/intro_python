import re

''' This method counts the amount of wins and draws between the two players
and stores the results in a size 3 list. index 0 is the draws, index 1 is
the wins for player 1 (alice), index 2 is the wins for player 2 (bob).'''
def compare(a, b):
    scores = [0,0,0]

    # iterate over
    for i in range(3):
        # Convert the score difference into the actual index to increment.
        index = a[i] - b[i]
        # try-catch to stop the program from crashing on zero division and
        # to rewrite the behaviour of dividing by zero for our advantage.
        try:
            index //= abs(index)
        except ZeroDivisionError:
            index = 0
        scores[index] += 1

    return scores[1:]


''' Method prompts user for input for the score from the given
person and the number of the score. It thre verifies the input
and prompts the user for new input if the previous was wrong'''
def get_input_regex(name):
    # have to check if it is a int, since i have to do it simpler, try-catch
    s = None
    pattern = re.compile(r'^((100|[1-9]\d|\d)\s){2}(100|[1-9]\d|\d)$')

    # 100, 10-99 or 0-1 space
    while s == None:
        s = input(F"Please enter the scores for {name}: ")
        if pattern.match(s):
            s = list(map(int, s.split(" ")))
        else:
            msg = "please ensure that you have entered 3 numbers, \n"
            msg += "each seperated by one space \n"
            msg += "and each in the range of 0 and 100 (inclusive)"
            print(msg)
            s = None
    return s


''' This gets the input from the user and checks if it is valid, if not
it prompts the user to try again and gives insight into the reason, too
short or not digits depending on the problem.
RETURNS the list of scores'''
def get_input_standard(name):
 # This loop only exits when a valid number is entered
    s = None
    while s == None:
        try:
            print(F"Please enter the scores for {name}")
            s = list(map(int, input().split()))
        except ValueError:
            # int with throw an error is string is not a number, so this keeps the program running
            # should of done this for zero div in calculator
            print("Please note that this input is invalid, please only enter 3 numbers seperated by a space")
            s = None
        #check length:
        if len(s) == 3:
            #make sure each index is in the range of 0-100
            for i in range(3):
                x = s[i]
                if x < 0 or x > 100:
                    print("Please ensure that numeric values are between 0 and 100 (inclusive)")
                    s = None
                    break
        # not 3 values
        else:
            print("please make sure you enter 3 values seperated by spaces")
            s = None
    return s


''' This is the main, the driver, if you will, for this file. '''
def main():
    #start with prompting user for scores
    alice =  get_input_regex("Alice")
    bob = get_input_regex("Bob")

    # COMMENT THE ABOVE LINES AND UNCOMMENT THE BELOW TO SEE THE DIFFERENCE

    #alice = get_input_standard("Alice")
    #bob = get_input_standard("bob")

    # eval
    scores = compare(alice, bob)

    # alice wins is in scores[1], bob's is in scores[2], ties in scores[0]
    print(F"Alices's score is {scores[0]}" "\n" F"Bob's score is {scores[1]}")



if __name__ == '__main__':
    main()
