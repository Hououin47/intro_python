class Grid:
  X = 'X'
  O = 'O'
  EMPTY = ' '

  rows = {
    0:[0,1,2], 1:[3,4,5], 2:[6,7,8]
  }

  cols = {
    0:[0,3,6], 1:[1,4,7], 2:[2,5,8]
  }

  diag = {
    1:[0,4,8], 2:[2,4,6]
  }

  def __init__(self):
    ''' Initialization method '''
    self.grid = [[self.EMPTY]*3, [self.EMPTY]*3, [self.EMPTY]*3]
    self.last_placed = None
    self.last_position = None
    self.row = None
    self.col = None
    self.won = None


  def __getitem__(self, position):
    ''' Getter for obect for easy updating of cells based on input method'''
    return self.grid[position // 3][position % 3]


  def __setitem__(self, position, piece):
    ''' Setter for obect for easy updating of cells based on input method'''
    self.row = position//3
    self.col = position%3
    self.last_placed = piece
    self.last_position = position
    self.grid[self.row][self.col] = piece


  def __str__(self):
    ''' Basic string representation of object '''
    return '\n---------\n'.join(' | '.join(row) for row in self.grid)


  def place_and_check(self, piece, position):
    ''' Checks if place is valid and them places '''
    # status message
    msg = ''
    # check if valid:
    isValid = True
    isValid, msg = self.valid(piece, position)
    if isValid:
      #place piece
      self[position] = piece
    # add an else for more shit. otherwise refactor
    return isValid, msg


  def is_won(self):
    ''' returns whether or not grid is won '''
    if self.won:
      return True
    return False


  def get_winner(self):
    ''' returns thewinner of grid '''
    return self.won


  def get_position(self):
    ''' getter for position played '''
    return self.last_position


  def get_last_played(self):
    ''' Returns last piece played '''
    return self.last_placed


  def game_over(self, position):
    ''' checks if game is over '''
    row = False
    col = False
    diag_1 = False
    diag_2 = False
    over = False

    # check row
    r = self.rows[self.row]
    row = self.check(r)

    # check col
    c = self.cols[self.col]
    col = self.check(c)

    # see which diag has to be tested and test
    if position%2 == 0:
      # even and it falls on diagonal
      if self.row == self.col:
        # one diag has the same row and col coords:
        d_1 = self.diag[1]
        if position == 4:
          # place on center, check both diags
          d_2 = self.diag[2]
        diag_1 = self.check(d_1)
      else:
        # other diagonal:
        d_2 = self.diag[2]
        diag_2 = self.check(d_2)
    # compare if any flags are set to true.
    over =  row or col or diag_1 or diag_2

    #set the won flag in object for color print etc
    if over:
      self.won = self.last_placed
    #return
    return over


  def valid(self, piece, position):
    valid = True
    msg = ''
    if self[position] != self.EMPTY:
      valid = False
      msg = 'Invalid Position. Select an empty spot'
    # add ore cases later
    return valid, msg


  def still_space(self):
    ''' Checks if theres available space to play '''
    for i in range(9):
      if self[i] == self.EMPTY:
        return True
    return False


  def check(self, line):
    ''' checks the line if its won '''
    for l in line:
      if self[l] != self.last_placed:
        return False
    return True


  def update(self, piece):
    ''' Updates piece for multiple board use '''
    self.last_played = piece
