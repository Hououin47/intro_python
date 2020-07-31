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


def make_grid(n):
    ''' fills in the numbers of the grid, from n to n+41 '''
    #initialize 6x7 array
    grid = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7]
    for i in range(6):
        for j in range(7):
            grid[i][j] = n
            n += 1
    return grid


def print_grid(grid):
    ''' prints the grid with the digits right justified '''
    # Iterate through 2d array and print values 
    for row in grid:
        i = 0
        for col in row:
            # set up the strings to change the color
            color = F"\x1b[6;{(31+i)};40m"
            reset = "\x1b[0m"
            print(F'{color}{col:>2}{reset}', end=' ')
            i += 1
        print()


def main():
    ''' main method '''
    n = get_input()
    mat = make_grid(n)
    print_grid(mat)


if __name__ == '__main__':
    main()
