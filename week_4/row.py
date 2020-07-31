import re

def get_input():
    ''' prompts user for input and validates it. if the constraints on n change, simple change the regex'''
    pattern = re.compile(r'^([-]?[0-5]|[6-9]|[1-8]\d|9[0-2])$')
    n = None
    while n == None:
        n = input("Enter the start number: ")
        if pattern.match(n):
            n = int(n)
        else:
            print("Please enter a number between -5 and 92")
            n = None
    return n


def make_list(n):
    ''' makes the  list containing the numbers of '''
    l = [0]*7
    for num in range(n, n+7):
        index = num-n
        l[index] = num
    return l


def print_list(l):
    ''' prints the list containing the seven numbers with pretty colors and rights justification and all on a single line'''
    for i in range(7):
        # set up the strings to change the color
        color = F"\x1b[6;{(31+i)};40m"
        reset = "\x1b[0m"

        msg = F"{color}{l[i]:>2}{reset}"
        print(msg, end=' ')
    print()


def main():
    ''' main ''' 
    n = get_input()
    l = make_list(n)
    print_list(l)


if __name__ == '__main__':
    main()
