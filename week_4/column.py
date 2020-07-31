import re

def get_input():
    ''' prompts user for input and validates it. if the constraints on n change, simple change the regex'''
    pattern = re.compile(r'^([-][2-5])|[-]?[0-1]$')
    n = None
    while n == None:
        n = input("Enter the start number: ")
        if pattern.match(n):
            n = int(n)
        else:
            print("Please enter a number between -5 and 1")
            n = None
    return n


def make_list(n):
    ''' makes the  list containing every seventh number between n adn n+41'''
    # This loop always runs 6 times til out of bounds
    l = [0]*6
    for i in range(6):
        l[i] = n+(i*7)
    return l


def print_list(l):
    '''prints out the list in lovely different colors, and right justification'''
    for i in range(len(l)):
        # set up the strings to change the color
        color = F"\x1b[6;{(31+i)};40m"
        reset = "\x1b[0m"

        msg = F"{color}{l[i]:>2}{reset}"
        print(msg)
    print()


def main():
    ''' main '''
    n = get_input()
    l = make_list(n)
    print_list(l)


if __name__ == '__main__':
    main()
