import re

# global variables
time_string = ''

''' Get the inputed time and create string '''
def get_time():
    global time_string
    time_string += (input("please enter hours: ") + ":")
    time_string += (input("please enter minutes: ") + ":")
    time_string += input("please enter seconds: ")


''' evaluates the inputed string with the pattern to see if valid '''
def evaluate(pattern):
    global time_string
    if pattern.match(time_string):
        return True
    else:
        return False


''' main '''
def main():

    # Set up variables
    pattern = re.compile(r'^(([0-1]\d|[2][0-3]):([0-5]\d):([0-5]\d))$')
    valid = True

    #get inpur and evaluate
    get_time()
    valid = evaluate(pattern)

    if valid:
        print("\x1b[6;32;40m Valid! \x1b[0m")
    else:
        print("\x1b[6;31;40m Invalid! \x1b[0m")


if __name__ == '__main__':
    main()
