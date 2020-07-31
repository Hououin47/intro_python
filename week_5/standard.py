import grid

players = ['O', 'X']

def print_board(board):
    '''replaces "x" with a red one and "o" with a blue one
    the prints the string representation of the board'''
    global players
    board = board.replace('X', '\x1b[0;31;40mX\x1b[0m')
    board = board.replace('O', '\x1b[0;36;40mO\x1b[0m')
    board = board.replace('|', '\x1b[0;33;40m|\x1b[0m')
    board = board.replace('-', '\x1b[0;33;40m-\x1b[0m')
    print(board)


def prompt():
    ''' Give instructional prompt '''
    msg = "Welcome to Tic Tac Toe.\nYou should know how to play it.\n"
    msg += "Please not that to play a move, one must select a position to play"
    msg += " between 0 and 8 inclusive. The positions are as follows:\n"
    msg += "\t0 | 1 | 2\n\t---------\n\t3 | 4 | 5\n\t---------\n\t6 | 7 | 8\n"
    print(msg)


def get_input(player):
    ####      remember to validate and add more instructions
    move = input(F'Player {player}, please enter move: ')
    return int(move)

def main():
    '''main'''
    global players
    index = 0
    board = grid.Grid()
    isRunning = True
    prompt()
    while isRunning:
        player = players[index]
        # get input/prompt player
        move = get_input(player)

        valid, msg = board.place_and_check(player, move)

        if valid:
            print_board(str(board))
            #move has already been placed, check if game over
            if board.game_over(move):
                isRunning = False
                print(F'Player {player} has won the game')
            elif not board.still_space():
                print("Its a Draw!!")
                isRunning = False
            # move index and modulo for wrap around
            index = (index + 1)%2
        else:
            print("Invalid move, try again")



if __name__ == '__main__':
    main()
