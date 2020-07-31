import string
from random import choice, random, uniform, sample
import re

''' Method to create a random password with at least: one uppercase
letter, one lowercase letter, one digit and one special character.
and length 8. The final password is the shuffled once more and returned'''
def create_password():
    sample = ''
    data = {
        0:string.ascii_lowercase, 1:string.ascii_uppercase,
        2:string.digits, 3:string.punctuation
    }

    #loop through dict to definitely get one of each
    for d in data:
        i = int(uniform(0,1)*4)
        # adds one of each group by end of loop
        sample += choice(data[d])
        # add a random choice of character
        sample += choice(data[i])


    return sample


''' method to get input on strength of password, then checks is valid
if not, prompts the user again'''
def get_difficulty():
    d = None
    pattern = re.compile(r'^[1-3]$')
    print("A WEAK password is 8 digits with at least one of the following: lowercase, uppercase, digit, special character")
    print("A MEDIUM one is 16 digits and at least 2 of the above")
    print("Finally, a STRONG password is 24 characters and at least 3 of each group\n\n")
    #run loop while input is invalid
    while not d:
        d = input("Please enter your password strength 1 for weak, 2 for medium and 3 for strong: ")
        if not pattern.match(d):
            print("please only enter one of the numbers 1 to 3")
            d = None
    return int(d)

''' builds sample of password to correct length and returns the shuffled random password '''
def set_up():
    strength = get_difficulty()
    s = ''

    #run for the corresponding amount of times to get length
    for i in range(strength):
        s += create_password()

    # the problem with this code is the every index is predictable in the
    # sense that we know which group it belongs to. to fix this, we
    # have to shuffle the string.
    password = ''.join(sample(s, len(s)))
    return strength, password


''' Main method to ask user for recuired strength and
display the returned password and the strength selected'''
def main():

    # set up variable to use for formatted printing
    diff = {1:"WEAK", 2:"MEDIUM", 3:"STRONG"}

    #get strength and password
    strength, password = set_up()

    msg = F"The chosen strength was {strength}, the outputed password should be"
    msg += F" of length {strength*8}." "\nThe returned Password is: \n"
    msg += F"\x1b[6;32;40m {password} \x1b[0m"
    print(msg)


if __name__ == '__main__':
    main()
