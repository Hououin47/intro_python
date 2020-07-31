import re

''' prompts user for input and only returns the int(year) once it is verified
as correct, otherwise the user is prompted to input a valid year again.'''
def get_year(pos):
    # make sure the input is valid and then return it to be used in calculations
    year = None
    while not year:
        year = input(F"Please enter the {pos} year (1000 - 9999): ")
        if not verify(year):
            year = None
    return int(year)


''' just verifies that the input is a 4digit number. If there are other year
constraints, the code can simply be edited by replacing the regex'''
def verify(year):
    # verify general years from 100
    pattern = re.compile(r'^(\d\d\d\d)$')
    if pattern.match(year):
        return True
    else:
        return False


'''Performs the formula thats provided. for ease of reading, the function is
passed year-1 instead of the year because year is not used in the formula
RETURNS the number corresponding to a day, as per formula'''
def calc(y):
    a = y%4
    b = y%100
    c = y%400
    # split the equation up to make it easier
    day = (1+5*a+4*b+6*c)%7
    return day


'''main method to set up and print what the output is. Contains a dict of
numbers to weekdays so an english string can be printed'''
def main():
    # dict to store days for f string , could be a list, but this is just..
    # explicit so you can see whats going on
    week = {
        0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday",
        4:"Thursday", 5:"Friday", 6:"Saturday"
    }

    year_1 = get_year("start")
    year_2 = get_year("end")
    
    for year in range(year_1, year_2+1):
        day = calc(year-1)
        print(F"The 1st of January {year} falls on a \x1b[6;33;40m {week[day]} \x1b[0m.")


if __name__ == '__main__':
    main()
