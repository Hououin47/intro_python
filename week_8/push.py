# module for 2048

from functools import  reduce


def push_left(grid):
    ''' Merge grid values left '''
    list(map(push, grid))


def push_right(grid):
    ''' Merge grid values right '''
    list(map(reverse_row, grid))
    list(map(push, grid))
    list(map(reverse_row, grid))


def push_up(grid):
    ''' Merge grid values upwards '''
    colonize(grid)
    list(map(push, grid))
    colonize(grid)


def push_down(grid):
    ''' Merge grid values downwards '''
    colonize(grid)
    list(map(reverse_row, grid))
    list(map(push, grid))
    list(map(reverse_row, grid))
    colonize(grid)


def merge(first, comp):
    '''function that does the merge on row'''
    # first element of row, 'first' empty list:
    if not first:
        first.append(comp)
        return first
    # compare last element in 'done' list and the comp variable
    if first[-1] == comp:
        # equal so merge
        first[-1] = comp*2
        # se next val to zero for 'lost' one
        comp = 0
    # append comp if different or 0 if not (to simulate lost index and stop adding to this)
    first.append(comp)
    return first


def push(row):
    ''' removes all zeros and adds adjacent like terms as per rules '''
    final = []

    # function for removing zeros from list
    no_zero = lambda x: x != 0

    #remove spaces:
    adj = list(filter(no_zero, row))
    final = list(reduce(merge, adj, final))

    #remove buffer zeros
    final = list(filter(no_zero, final))

    #add zeros if needed:
    final.extend([0]*(4-len(final)))
    row[:] = final


def colonize(grid):
    # map to list not necissary, but doing for con
    grid[:] = list(map(list, zip(*grid)))


def reverse_row(row):
    row[:] = row[::-1]
