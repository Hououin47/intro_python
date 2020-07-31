from functools import reduce
from copy import deepcopy


def create_grid(grid):
    '''create a 4x4 array of zeroes within grid'''
    for i in range(4):
        grid.append([0,0,0,0])


def print_grid (grid):
    '''print out a 4x4 grid in 5-width columns within a box'''
    string = ''
    solid =  "\x1b[0;37;47m \x1b[0m"
    for i in range(4):
        string += ((F"{solid}"*5)*6+'\n')
        string += (F"{solid}{solid}     "*5+'\n')
        for j in range(4):
            string += F"{solid}"*2
            x = grid[i][j]
            if x != 0:
              string += F"{x:>5d}"
            else:
              x = ' '
              string += F"{x:>5s}"
        string += F"{solid}"*2+"\n"
        string += (F"{solid}{solid}     "*5+'\n')
    string += ((F"{solid}"*5)*6+'\n')
    print(string)



def check_lost (grid):
    '''return True if there are no 0 values and there are no adjacent values
    that are equal; otherwise False'''

    # check if zero, check won can check for any value:
    space = check_won(grid, 0)
    adj = False

    # check for adj vals
    for g in range(16):
        i = g//4
        j = g%4
        val = grid[i][j]
        adj_pos = adjacent(i,j)
        for a in adj_pos:
            if grid[a[0]][a[1]] == val:
                # there is an adjacent value, so break both loops
                adj = True
                g = 17
    # return true if either true
    res = not space and not adj
    return res


def check_won (grid, val=32):
    '''return True if a value>=32 is found in the grid; otherwise False'''
    cmp_ = lambda x, y: x or y
    # Check if any rows contain 32
    status = [True if val in row else False for row in grid]
    # true is at least one row contains 32
    win = reduce(cmp_, status)
    return win


def copy_grid (grid):
    '''return a copy of the given grid'''
    c_list = deepcopy(grid)
    return c_list


def grid_equal (grid1, grid2):
    '''check if 2 grids are equal - return boolean value'''
    #zip for easy iteration
    cmp_ = lambda x, y: x and y
    compare = zip(grid1, grid2)
    status = [True if r1 == r2 else False for r1, r2 in compare]
    eq = reduce(cmp_, status)
    return eq


def adjacent(x, y):
    ''' gets the adjacent cell positions of the current position in the grid '''
    adj = lambda pos: (pos[0] >= 0 and pos[0] < 4) and (pos[1] >= 0 and pos[1] < 4)
    neighbours = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    neighbours = list(filter(adj, neighbours))
    return neighbours
