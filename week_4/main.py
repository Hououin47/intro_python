import column, grid, printmonth, row, palindromeprime

''' Just a normal main '''
def main():
    isRunning = True

    print("Enter the numbers 1 to 4 for the corresponding question and 'EXIT' to stop program\n")

    while isRunning:
        ex = input("Please enter the number of the question you with to run: ")
        ex.strip()
        
        begin = ("\n" F"_________BEGIN QUESTION {ex}______" "\n")
        end = ("\n" F"_________END QUESTION {ex}______" "\n")
        if ex == '1':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            row.main()
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == '2':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            column.main()
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == '3':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            grid.main()
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == '4':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            printmonth.main()
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == '5':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            palindromeprime.main()
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == 'EXIT':
            print(F"___________EXITING__________")
            isRunning = False
        else:
            print("you've entered an invalid answer, try again")


if __name__ == '__main__':
  main()