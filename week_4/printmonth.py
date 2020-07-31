''' Global variables to get array index of day and  length ot month '''
days = {
    'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3,
    'Friday':4, 'Saturday':5, 'Sunday':6
    }
months = {
    'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
    'July':31, 'August':31, 'September':30, 'October':31, 'November':30,
    'December':31
}



def print_month(month):
    ''' Prints a month created month array onto the calendar format. '''
    # print days above
    print("\n\x1b[6;34;40mMo Tu We Th Fr Sa Su\x1b[0m\n")

    # loop through and print date in array
    for row in month:
        i = 0
        for col in row:
            color = F"\x1b[6;{(31+i)};40m"
            reset = "\x1b[0m"
            if col == 0:
                print('  ', end=' ')
            else:
                print(F'{color}{col:<2}{reset}', end=' ')
            i += 1
        print('\n')


def get_input():
    ''' Prompts user for the required information, validates it and returns the information in int format for the program to use '''
    global months, days
    isRunning = True
    start = None
    length = None
    day = None
    month = None
    while isRunning:
        #get input
        month = input("Please enter the month ('January', ... , 'December'): ")  
        day = input("Enter the start day ('Monday', ... , 'Sunday'): ")
        #get the corresponding value from the global dicts
        start = days.get(day, None)
        length = months.get(month, None)
        #check if both are valid
        if length == None or start == None:
            print("Please ensure that the input is valid")
        else:
            isRunning = False
    return start, length


def make_month(start, end):
    ''' Creates the month array to be printed or whatever you want with it.'''
    # initializes the 6x7 matrix for the calendar.
    # empty spaces before and after for ease of printing
    month = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7]
    day = 1

    #each item in list has the date. 0 is an epty space for start/end.
    for i in range(start, start+end):
        row = i//7
        col = i%7
        month[row][col] = day
        day += 1
    return month


def main():
    ''' main method to run the program '''
    start, end = get_input()
    month = make_month(start, end)
    print_month(month)


if __name__ == '__main__':
    main()
