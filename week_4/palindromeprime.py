from math import ceil, floor

def get_input(pos):
    ''' gets input and validates it '''
    output = None

    while output == None:
        output = input(F"Pease enter the {pos} number: ")
        try:
            output = int(output)
        except ValueError:
            output = None
            print("Please enter a number")
    return output


def create_primes(start, end):
    ''' creates the list containing prime numbers in the given range '''
    # Initialize a list
    primes = []
    for possiblePrime in range(max(2, start), end+1):

        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)
    return primes


def is_palindrome(prime):
    ''' checks if given string is a palindrome '''
    #make a string
    isValid = False
    prime = str(prime)
    length = len(prime)

    # if we use ceil and floor, we do not have to account
    # for the 'middle' character in the case of an odd lenght string

    # end of first substring (exclusive)
    a = floor(length/2)
    # begining of second substring (inclusive)
    b = ceil(length/2)

    text_1 = prime[:a]
    text_2 = prime[b:][::-1]

    if text_1 == text_2:
        isValid = True
    return isValid


def create_palindrome_list(primes):
    ''' Filters the list and returns a list only containing palindrome-primes '''
    palindromes = [p for p in primes if is_palindrome(p)]
    return palindromes


def print_palindromes(palindromes, start, end):
    ''' Prints the palindroms ii color, alternating each one and printing
the matching sides in a color and the middle (if odd length) in another'''

    #if empty, print message saying so and exit
    if len(palindromes) == 0:
        print(F"\x1b[0;37;41m There are no palindrome primes between {start} and {end}\x1b[0m")
        return

    i = 0
    for prime in palindromes:
        #define the two colors:
        color_match = F"\x1b[6;{31+(i%7)};40m"
        color_middle = F"\x1b[6;{31+((i+5)%7)};40m"
        reset = "\x1b[0m"
        prime = str(prime)
        length = len(prime)
        a = floor(length/2)
        b = ceil(length/2)

        text_1 = prime[:a]
        text_2 = prime[b:]
        text_3 = prime[a:b]

        # create color string to print:
        msg = F'{color_match}{text_1}{reset}{color_middle}{text_3}{reset}'
        msg += F'{color_match}{text_2}{reset}'
        print(msg)
        i += 1


def main():
    ''' normal main '''
    start = get_input("Starting")
    end = get_input("Ending")

    primes = create_primes(start, end)
    palindromes = create_palindrome_list(primes)

    print_palindromes(palindromes, start, end)


if __name__ == '__main__':
    main()
