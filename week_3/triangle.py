from math import sqrt

''' Method to get input from user, and checks if the format is correct.
i.e a integer or float, if non are inputed, the user will be prompted
 to input another one'''
def get_input(name):
    # have to check if it is a float, since i have to do it simpler, try-catch
    side = None

    # This loop only exits when a valid number is entered
    while side == None:
        try:
            side = input(F"Please input the length fo side {name}: ")
            side = float(side)
        except ValueError:
            # float with throw an error is string is not a number, so this keeps the program running
            # should of done this for zero div in calculator
            print("Please note you have to enter a number")
            side = None
    return side


''' performs the given formula to get the area of a triangle with sides a, b, c. '''
def calc(a, b, c):
    #define smaller pieces of equation
    s = (a + b + c)/2
    diff = [s-a, s-b, s-c]

    # try as best to automate and create area in a nice readable fashion
    area = s
    for d in diff:
        area *= d
    area = sqrt(area)

    # return it
    return area


''' Main to handle everything '''
def main():
    a = get_input("A")
    b = get_input("B")
    c = get_input("C")

    ans = calc(a, b, c)

    print(F"The area of the triangle with lengths {a}, {b} and {c} is {ans:.2f}")


if __name__ == '__main__':
    main()
