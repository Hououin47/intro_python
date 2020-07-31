''' Global variables to get array index of day and  length ot month '''
days = {
    1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 0:'Sunday'
    }
months = {
    1:['January',31], 2:['February',28, 29], 3:['March',31], 4:['April',30],
    5:['May',31], 6:['June',30], 7:['July',31], 8:['August',31],
    9:['September',30], 10:['October',31], 11:['November',30], 12:['Decenber',31]
}


def is_leap_year(year):
    '''checks if year is leap year'''
    leap = False
    four = year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap = True
    return leap


def days_in_month(month_number, year):
    ''' returns number of days in month leap years included'''
    global months
    index  = 1
    if is_leap_year(year):
        index = -1

    days = months.get(month_number, "Invalid month!")
    return days[index]


def month_name(number):
    ''' method to get name of month from number '''
    global months
    month = months.get(number, "Invalid month!")
    return month[0]


def first_day_of_year(year):
    '''Performs the formula thats provided. The formula RETURNS the number corresponding to a day, as per formula'''
    y = year - 1
    a = y%4
    b = y%100
    c = y%400
    # split the equation up to make it easier
    day = (1+5*a+4*b+6*c)%7
    return day


def first_day_of_month(month_number, year):
    ''' Returns number related to the first day of month for year. Leap yers included'''
    start = first_day_of_year(year)
    days = 0
    # add the other months
    for i in range(1, month_number):
        days += days_in_month(i, year)

    # work out what day it is mod 7 num system (0-6),
    end = start + days
    end %= 7
    return end

def get_num(msg, y=False):
  '''simple verification and input method'''
  num = None
  while num == None:
    num = input(msg)
    if y:
      if len(num) != 4:
        num = None
    try:
      num = int(num)
    except ValueError:
      num = None
      print("Please enter a valid number!")
    except TypeError:
      num = None
      print("Please enter a valid number!")
  return num

def main():
  ''' main '''
  global days
  isRunning = True
  while isRunning:
    msg = 'Choose from the following options:\n0. quit\n1. Test is_leap_year().\n2. Test month_name().\n3. Test days_in_month().\n4. Test first_day_of_year().\n5. Test first_day_of_month().\n'

    rep = input(msg)
    if rep == '0':
      isRunning = False
    elif rep == '1':
      year = get_num("Please input 4 digit year: ", True)
      if is_leap_year(int(year)):
        print(F"The year {year} is a leap year")
      else:
        print(F"The year {year} is not a leap year") 
    elif rep == '2':
      for i in range(1, 13):
        print(F"Month number {i} is {month_name(i)}")
    elif rep == '3':
      year = get_num("Please input 4 digit year: ", True)
      month = get_num("Please enter a month number: ")
      m = month_name(month)
      amount = days_in_month(month, year)
      print(F"The amount of days in {m} {year} is {amount}")
    elif rep == '4':
      year = get_num("Please input 4 digit year: ", True)
      day = first_day_of_year(year)
      print(F"The the first of january {year} falls on a {days[day]}")
    elif rep == '5':
      year = get_num("Please input 4 digit year: ", True)
      month = get_num("Please enter a month number: ")
      m = month_name(month)
      day = first_day_of_month(month, year)
      print(F"The the first of {m} {year} falls on a {days[day]}")
    else:
      print("Invalid option")
