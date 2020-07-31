import grid
import re
# Super Tic Tac Toe

''' Global variables '''
board_outer = []

avail = [0,1,2,3,4,5,6,7,8]    # init for all cells avail:

rows = {
    0:[0,1,2], 1:[3,4,5], 2:[6,7,8]
  }

cols = {
    0:[0,3,6], 1:[1,4,7], 2:[2,5,8]
  }

diag = {
    1:[0,4,8], 2:[2,4,6]
  }
players = ['O', 'X']


def prompt():
    ''' Give instructional prompt '''
    msg = "Welcome to Tic Tac Toe.\nYou should know how to play it.\n"
    msg += "Please note that to play a move, one must select a position to play"
    msg += " between 0 and 8 inclusive. The positions are as follows:\n"
    msg += "\t0 | 1 | 2\n\t---------\n\t3 | 4 | 5\n\t---------\n\t6 | 7 | 8\n"
    msg += "This applies for both the outer and inner grids. Please read"
    msg += " the PDF for instructions\n\n"
    print(msg)


def get_input(msg):
    ''' Gets position and validates '''
    pat = re.compile(r'^[0-8]$')
    pos = None
    while pos == None:
        pos = input(msg)
        if not pat.match(pos):
            pos = None
    return int(pos)


def update_avail(pos):
    global board_outer, avail
    avail = []
    # if square is won, any non-won square avail
    if board_outer[pos].is_won():
        for i in range(9):
            if not board_outer[i].is_won():
                avail.append(i)
    else:
        avail.append(pos)


def populate(board):
    ''' initiates outer grid a smaller grid in each cell '''
    for i in range(9):
        board.append(grid.Grid())
    return board


def update_piece(piece):
    '''Loops through grid objectts and syncs the last played piece'''
    global board_outer
    for i in range(9):
        board_outer[i].update(piece)


def legal(pos):
    ''' checks if outer grid placement is legal '''
    global avail
    if pos in avail:
        return True
    return False


def game_over(position, piece):
    ''' Checks if game is over '''
    global rows, cols, diag
    row = False
    col = False
    diag_1 = False
    diag_2 = False
    over = False

    r_index = position//3
    c_index = position%3

    # check row
    r = rows[r_index]
    row = check(r, piece)
    # check col
    c = cols[c_index]
    col = check(c, piece)

    # see which diag has to be tested and test
    if position%2 == 0:
        # even and it falls on diagonal
        if r_index == c_index:
        # one diag has the same row and col coords:
            d_1 = diag[1]
            if position == 4:
          # place on center, check both diags
                d_2 = diag[2]
            diag_1 = check(d_1, piece)
        else:
        # other diagonal:
            d_2 = diag[2]
            diag_2 = check(d_2, piece)
    # compare if any flags are set to true.
    over =  row or col or diag_1 or diag_2
    #set the won flag in object for color print etc
    return over


def check(line, piece):
    ''' checks the line if its won '''
    global board_outer
    for l in line:
        winner = board_outer[l].get_winner()
        if winner != piece:
            return False
    return True


def get_row(grid, p):
    ''' Helper method to get a row over 3 grid objects'''
    msg = []
    for r in range(9):
        pos = r%3

        cell = grid[pos]
        start = 3*(r//3)
        end = start+3
        for i in range(start, end):
            x = color(cell,(3*p+pos), i)
            msg.append(x)
    return msg


def print_board():
    ''' prints out the board, since each objects string has new lines, have to edit remove etc '''
    global board_outer
    long_row = []
    solid = "\x1b[0;37;47m \x1b[0m"
    for i in range(3):
        start = (i)*3
        end = start+3
        row = board_outer[start:end]
        long_row += get_row(row, i)

    for i in range(81):
        if i%9 == 0 and i != 0:
            if i%27 == 0:
                print("\n"+solid*23)
            else:
                print()
        if i%3 == 0 and i != 0 and i%9 != 0:
            print(solid*2, end = " ")
        print(long_row[i], end = " ")
    print()


def color(cell, position, i):
    global avail
    # define colors
    x = '\x1b[0;31;40m'
    o = '\x1b[0;34;40m'
    x_won = '\x1b[0;37;41m'
    o_won = '\x1b[0;37;44m'
    av = '\x1b[0;37;43m'
    reset = '\x1b[0m'
    output = ''
    if cell.get_winner() == 'X':
        output += x_won
    elif cell.get_winner() == 'O':
        output += o_won
    elif position in avail:
        if cell[i] == 'X':
            output += x
        elif cell[i] == 'O':
            output += o
        else:
            output += av
    else:
        if cell[i] == 'X':
            output += x
        elif cell[i] == 'O':
            output += o
    output += cell[i]
    output += reset
    return output


def display():
    global board_outer
    for cell in board_outer:
        print(cell.is_won())
        print(cell)


def init():
    ''' Starts game '''
    global board_outer, players
    #set up board
    populate(board_outer)
    print_board()
    isRunning = True
    piece = None
    index = 1
    msg = ''
    outer = None
    prompt()

    # user gets to choose first big square:
    while isRunning:
        piece = players[index]
        if len(avail) > 1:
            outer = get_input(F"Player {piece}. Please enter the position of the outer suare you wish to start in: ")
        if legal(outer):
            pos = get_input(F"Player {piece}. Please enter a position in the inner grid: ")
            board = board_outer[outer]
            valid, msg = board.place_and_check(piece, pos)
        else:
            valid = False
        if valid:

            # check if the move won a cell:
            won = board.game_over(outer)
            # if it did, check the outer cells for victory
            if won:
                if game_over(outer, piece):
                    isRunning = False
                    break
            # update avail squares:
            outer = board.get_position()
            update_piece(piece)
            update_avail(outer)
            # move index and modulo for wrap around
            index = (index + 1)%2
            # update outer

        else:
            print("Please place a valid move")
        print_board()
    print(F"Plaer {piece} has won")
    print('Final Board')
    print_board()


if __name__ == '__main__':
    init()
