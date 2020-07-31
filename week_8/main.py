import acronym



''' Just a normal main '''
def main():
    isRunning = True

    print("Enter the numbers 1 to 3 for the corresponding question and 'EXIT' to stop program\n")

    while isRunning:
        ex = input("Please enter the number of the question you with to run: ")
        ex.strip()
        
        begin = ("\n" F"_________BEGIN QUESTION {ex}______" "\n")
        end = ("\n" F"_________END QUESTION {ex}______" "\n")
        if ex == '1':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            acronym.main()
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == '2':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            import testutil
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == '3':
            print(F"\x1b[6;33;40m {begin} \x1b[0m")
            import game
            print(F"\x1b[6;33;40m {end} \x1b[0m")
        elif ex == 'EXIT':
            print(F"___________EXITING__________")
            isRunning = False
        else:
            print("you've entered an invalid answer, try again")


if __name__ == '__main__':
  main()



