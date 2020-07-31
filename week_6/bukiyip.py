import re

def bukiyip_to_decimal(a):
    ''' converts a bukiyip number (base 3) to adecimal number (base 10) '''
    # convert to string to use slicing and reversed for easy looping
    buki = str(a)[::-1]
    l = len(buki)
    d = 0

    for i in range(l):
        #get number and factor of 3 to put back into decimal and sum them
        digit = int(buki[i])*pow(3, i)
        d += digit
    return d


def decimal_to_bukiyip(a):
    ''' Converts a decimal number (base 10) to a bukiyip number (base 3) '''
    buki = ''
    temp = ''
    while a:
        #get mod 3 of number
        m = a%3
        #use temp and switch so we bulid the number the correct way around
        temp = str(m)
        temp += buki
        buki = temp
        #get rid of factor we just 'used'
        a //= 3
    buki = int(buki)
    return buki


def bukiyip_add(a, b):
    ''' Adds two base 3 numbers and returns a base 3 number '''
    decimal_a = bukiyip_to_decimal(a)
    decimal_b = bukiyip_to_decimal(b)

    decimal_ans = int(decimal_a+decimal_b)
    bukiyip_ans = decimal_to_bukiyip(decimal_ans)
    return bukiyip_ans


def bukiyip_subtract(a, b):
    ''' Subtracts two base 3 numbers and returns a base 3 number '''
    decimal_a = bukiyip_to_decimal(a)
    decimal_b = bukiyip_to_decimal(b)

    decimal_ans = int(decimal_a-decimal_b)
    bukiyip_ans = decimal_to_bukiyip(abs(decimal_ans))
    if decimal_ans < 0:
      bukiyip_ans = -1*bukiyip_ans
    return bukiyip_ans



def bukiyip_multiply(a, b):
    ''' Multiplies two base 3 numbers and returns a base 3 number '''
    decimal_a = bukiyip_to_decimal(a)
    decimal_b = bukiyip_to_decimal(b)

    decimal_ans = int(decimal_a*decimal_b)
    bukiyip_ans = decimal_to_bukiyip(decimal_ans)
    return bukiyip_ans


def bukiyip_divide(a, b):
    ''' Multiplies two base 3 numbers and returns a base 3 number '''
    decimal_a = bukiyip_to_decimal(a)
    decimal_b = bukiyip_to_decimal(b)

    decimal_ans = int(decimal_a//decimal_b)
    bukiyip_ans = decimal_to_bukiyip(decimal_ans)
    return bukiyip_ans


def get_input(bukiyip=False):
  'Gets a number and verifies based on whether its a base 3 or 10 number.'
  pattern = re.compile(r'^[0-2]+$')
  k = None
  base = 'Base-10'
  if bukiyip:
    base = 'Base-3'
  while k == None:
    k = input(F"Plese enter a {base} number: ")
    if bukiyip:
      if pattern.match(k):
        k = int(k)
      else:
        k = None
        print("Please ensure that this is a legal base-3 number")
    else:
      try:
        k = int(k)
      except ValueError:
        k = None
        print("Please entern numbers only")
  return k


def main():
  ''' main '''
  isRunning = True
  print('Bukiyup program: ')
  print("'d' -> convert base-10 to base-3")
  print("'b' -> convert base-3 to base-10")
  print("'a' -> add two base-3 numbers")
  print("'s' -> subtract two base-3 numbers")
  print("'m' -> multiply two base-3 numbers")
  print("'v' -> integer division on two base-3 numbers")
  print("'q' -> exit program")

  while isRunning:
    rep = input("Enter a command: ")
    if rep == 'd':
      d = get_input()
      d_b = decimal_to_bukiyip(d)
      print(F"{d} converted to base-3 is {d_b}")
    elif rep == 'b':
      b = get_input(True)
      b_d = bukiyip_to_decimal(b)
      print(F"{b} converted to base-10 is {b_d}")
    elif rep == 'a':
      b_1 = get_input(True)
      b_2 = get_input(True)
      a = bukiyip_add(b_1, b_2)
      print(F"{b_1} + {b_2} = {a} (all in base-3)")
    elif rep == 's':
      b_1 = get_input(True)
      b_2 = get_input(True)
      s = bukiyip_subtract(b_1, b_2)
      print(F"{b_1} - {b_2} = {s} (all in base-3)")
    elif rep == 'm':
      b_1 = get_input(True)
      b_2 = get_input(True)
      m = bukiyip_multiply(b_1, b_2) 
      print(F"{b_1} * {b_2} = {m} (all in base-3)")
    elif rep == 'v':
      b_1 = get_input(True)
      b_2 = get_input(True)
      v = bukiyip_divide(b_1, b_2) 
      print(F"{b_1} / {b_2} = {v} (all in base-3)")
    elif rep == 'q':
      isRunning = False
    else:
      print("Invalid input")
