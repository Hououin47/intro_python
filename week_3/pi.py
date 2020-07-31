from math import sqrt


''' Method to approximate Pi to the given formula.
uses lambda to evaluate the formula.'''
def approx():
    # $make a lambda to store the function, kinda
    f = lambda x: sqrt(2 + x)

    #first itter when x = 0:
    x = 0

    # run the rest of the iters while it has to run..
    isRunning = True
    pi = 1
    while isRunning:
        x = f(x)
        pi *= x/2
        #check to break at end of loop
        if (x/2 == 1):
            isRunning = False
    return 2/pi


''' Gets input and makes sure it is valid. If wrong,
user is prompted for a correct input '''
def get_input():
    r = None
    while not r:
        r = input("please enter a radius: ")
        try:
            r = float(r)
        except ValueError:
            r = None
            print("please enter a number (Integer or Float)")
    return r


''' main method to set up all the required values like the pi approximation and
and getting the radius, then computing the area and formatted printing it.'''
def main():
    # Please not that i refuse to use round. I will keep the
    # values as correct as they are and format the printing
    pi = approx()
    r = get_input()

    # no parenthesis is needed because ** has higher priority
    area = pi*r**2

    msg = F"The approximation of pi is {pi:.3f}" "\n"
    msg +=F"The area of circle with radius {r} to 3 decimal places is:" "\n"
    msg += F"{area:.3f}"

    print(msg)


if __name__ == '__main__':
    main()
