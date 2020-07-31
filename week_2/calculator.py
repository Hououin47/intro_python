''' Instead of simply adding two numbers, this will be made into a
 Reverse Polish notation calculator. Keeping it ass a simple
 calculator as per decription, but giving it some functionality.'''

stack = [None, None, None]          #simple stack to accomodate 2 operators and an operand.

def get_ops():
    global stack
    stack[0] = float(input("Please enter first number: "))
    stack[1] = float(input("Please enter second number: "))
    stack[2] = input("Please enter operation: ")


def apply_ops():
    global stack
    op = stack[2]
    n2 = stack[1]
    n1 = stack[0]
    ans = 0.0

    msg = ""

    if (op == "+"):
        ans = n1 + n2
        msg = F"you entered {n1} {op} {n2}" "\n"
        msg += F"The answer is : {ans}"
    elif (op == "-"):
        ans = n1 - n2
        msg = F"you entered {n1} {op} {n2}" "\n"
        msg += F"The answer is : {ans}"
    elif (op == "*"):
        ans = n1 * n2
        msg = F"you entered {n1} {op} {n2}" "\n"
        msg += F"The answer is : {ans}"
    elif (op == "/"):
        ans = n1 / n2
        msg = F"you entered {n1} {op} {n2}" "\n"
        msg += F"The answer is : {ans}"
    else:
        msg = F"Invalid operand '{op};"

    return (msg, ans)


def main():
    get_ops()
    msg, ans = apply_ops()
    print(msg)
    #ans can be pushed back onto the stack in advanced cases


if __name__ == '__main__':
    main()
