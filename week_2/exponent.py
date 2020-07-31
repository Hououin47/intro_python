''' CHEAT WAY call pow(a,b)'''

def exponent(a, b):
    output = 1
    for i in range(b):
        output *= a
    return output


def main():
    base = None
    power = None
    while base == None:
        base = input("please enter the base number: ")
        if not str.isdigit(base):
            base = None
            print("Please onlt enter numbers")
        else:
            base = int(base)

    while power == None:
        power = input("please enter the power number: ")
        if not str.isdigit(power):
            power = None
            print("Please onlt enter numbers")
        else:
            power = int(power)
    ans = exponent(base, power)
    print(F"{base} to the power of {power} is equal to {ans}")


if __name__ == '__main__':
    main()
