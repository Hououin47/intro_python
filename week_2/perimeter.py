def get_vals():
    h1 = float(input("Enter height 1: "))
    h2 = float(input("Enter height 2: "))
    w1 = float(input("enter width 1: "))
    w2 = float(input("Enter width 2: "))
    price = float(input("Enter price per meter: "))
    return (h1, h2, w1, w2, price)


def print_info(length, cost):
    msg = F"The total fence required = {length:.2f} meters." "\n"
    msg += F"The total price = R {cost:.2f}"
    print(msg)


def calc(h1, w1, w2, price):
    #because the outer lines add up to (h1-h2) the expression cancels h2 out
    '''
    h1 + w1 + x + w2 + h2 + w2 + x + w1
    h1 + 2*w1 + 2*w2 + 2*x + h2
                                         ~let 2*x = (h1-h2)
    h1 + 2*w1 + 2*w2 + (h1 - h2) + h2
    2*h1 +2*w1 + 2*w2
    2*(h1 + w1 + w2)
    '''
    length = 2*(h1+w1+w2)
    cost = length*price
    return length, cost


def main():
    h1, h2, w1, w2, price = get_vals()
    length, cost = calc(h1, w1, w2, price)
    print_info(length, cost)


if __name__ == '__main__':
    main()
