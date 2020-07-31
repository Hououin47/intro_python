'''Advanced calculator, based of previous calculator. has option for a
normal calculator or RPN based list input'''

from collections import deque
isRunning = True
session = True


def start():
    global isRunning, session
    rpn = False
    std = False
    ses = input("Please enter 1 for RPN\n2 for normal caluctaor\nand 3 to exit\n>>> ")
    if ses == "1":
        rpn = True
        std = False
    elif ses == "2":
        std = True
        rpn = False
    elif ses == "3":
        session = False
        isRunning = False
    else:
        print("Invalid answer, Try again.")
        session = False
    return (std, rpn)


def calc(n1, n2, op):
    #verify:
    if (op == "+"):
        ans = n1 + n2
    elif (op == "-"):
        ans = n1 - n2
    elif (op == "*"):
        ans = n1 * n2
    elif (op == "/"):
        ans = n1 / n2
    else:
        ans = None
    return str(ans)


''' This method changes the inputed char to float if it is a digit '''
def identify(x):
    if str.isdigit(x):
        x = int(x)
    elif x == "+" or x == "-" or x == "/" or x == "*":
        x = x
    else:
        x = None
    return x


''' print contents of stack '''
def print_stack(stack):
    msg = ""
    if (len(stack) == 0):
        msg = "0"
    for x in stack:
        msg += (str(x) + " ")
    return (msg+ "\n")


''' This method is the one to run the "normal calculator '''
def normal():
    global session
    stack = deque()
    ans = 0
    isRunning = True
    while isRunning:
        x = input(F"{print_stack(stack)}>>> ")
        if x == "EXIT":
            isRunning = False
        elif x == "DEL":
            stack.pop()
        elif x == "CE":
            stack.clear()
        elif x == "=":
            n1 = stack.popleft()
            op = stack.popleft()
            n2 = stack.popleft()
            ans = calc(n1, n2, op)
            if (ans == None):
                ans = 0
                print("SYNTAX ERROR")
                stack.clear()
            stack.append(ans)
        else:
            x = identify(x)
            if x :
                stack.append(x)
            else:
                print("Invalid command!")
    print("Exited normal calculator")
    session = False


''' This prompt the user for the chain of operations in reverse polish notation '''
def get_list():
    x = input("Please enter operations seperated by a space and valid. Theres no error checking:\n")
    output = x.split(" ")
    return output

''' This method is the one to run the reverse polish calculator '''
def reverse_polish(instructions):
    global session
    print("Starting evaluation")
    stack  = deque()
    temp = None
    n2 = None
    n1 = None
    op = None
    for i in instructions:
        if str.isdigit(i):
            stack.append(int(i))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            op = i
            temp = calc(n1, n2, op)
            stack.append(int(temp))
    session = False
    print(F"Evaluation done, the answer is: {stack.pop()}")


'''This is where the code for the calculator sarts'''
def main():
    global isRunning, session
    isRunning = True
    session = True
    std = False
    rpn = False
    instauctions = []    #This is the instruction array for the RPN
    while isRunning:
        #loop to run application:
        std, rpn = start()      #see what mode etc.
        while session:
            if std:
                normal()
                std = False
            elif rpn:
                instructions = get_list()
                reverse_polish(instructions)
                rpn = False
        print("session done")
    print("Program exiting")


if __name__ == '__main__':
    main()
