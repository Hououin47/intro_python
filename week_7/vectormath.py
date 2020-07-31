class Vector:
    ''' Class for vectors '''

    def __init__(self, x = 0, y = 0, z = 0):
        ''' init '''
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, vector):
        ''' addition '''
        x = self.x + vector.x
        y = self.y + vector.y
        z = self.z + vector.z
        return Vector(x,y,z)


    def __sub__(self, vector):
        ''' subtraction '''
        x = self.x - vector.x
        y = self.y - vector.y
        z = self.z - vector.z
        return Vector(x,y,z)


    def __mul__(self, var):
        ''' Cross product and scalar multiplication both use * operator '''
        if isinstance(var, Vector):
          # cross product
          x = self.y*var.z - self.z*var.y
          y = self.z*var.x - self.x*var.z
          z = self.x*var.y - self.y*var.x
          return Vector(x,y,z)
        else:
          # scalar multiplication
          x = self.x * var
          y = self.y * var
          z = self.z * var
          return Vector(x,y,z)


    def norm(self):
        ''' norm/magnitude of a vector '''
        n = self.x**2
        n += self.y**2
        n += self.z**2
        n = pow(n, 0.5)
        return n

    def dot(self, vector):
        ''' Dot product '''
        x = self.x * vector.x
        y = self.y * vector.y
        z = self.x * vector.z
        return x+y+z


    def __str__(self):
        ''' string representation of object '''
        string = F"[{self.x:.2f}, {self.y:.2f}, {self.z:.2f}]"
        return string


def get_scalar():
    ''' prompts user for scalar value and verifies '''
    k = None
    while k == None:
        k = input("Please enter a scalar value: ")
        try:
            k = float(k)
        except ValueError:
            k = None
            print("Please enter a number")
    return k


def get_vector():
  ''' promts user for vector vals, returns tuple of x,y,z '''
  v = input('please enter your values for the vector seperated by a single space only: ')

  v = v.split(' ')
  return int(v[0]), int(v[1]), int(v[2])


def main():
  ''' main '''
  isRunning = True
  while isRunning:
      rep = input("Enter 0 to continue, 'quit' to exit: ")
      if rep == '0':
          print("vector 1")
          a,b,c = get_vector()
          print('vector 2')
          x,y,z = get_vector()
          v_1 = Vector(a,b,c)
          v_2 = Vector(x,y,z)
          k = get_scalar()
          add = v_1 + v_2
          sub = v_1 - v_2
          sc1 = v_1*k
          sc2 = v_2*k
          crs = v_1*v_2
          dot = v_1.dot(v_2)
          n1 = v_1.norm()
          n2 = v_2.norm() 
          print(F"A + B = {add}")
          print(F"A - B = {sub}")
          print(F"A * k = {sc1}")
          print(F"B * k = {sc2}")
          print(F"A x B = {crs}")
          print(F"A . B = {dot}")
          print(F"| A | = {n1}")
          print(F"| B | = {n2}")
      elif rep == 'quit':
          isRunning = False
      else:
          print("Invalid input")