'''So instead of simply printing out the shape, we can specify the height and length of it.'''

def print_shape(height, length):
    #predifine chars for ease of changing them
    astrix = "*"
    space = " "

    #use operator overloading of multiplication in strings to create 'lines'
    solid = astrix*length
    other = astrix+(space*(length-2))+astrix
    for i in range(height):
        if i == 0 or i == (height-1):
            print(solid)
        else:
            print(other)

def main():
    #main method, ask for dimensions, then print
    h = int(input("please enter the height of the shape: "))
    l = int(input("please enter the length of the shape: "))
    print_shape(h,l)


if __name__ == '__main__':
    main()
