from random import uniform

def select_random_phrase():
    ''' Method to select and return a random phrase '''
    phrases = ['Have you tried it on a different operating system?', \
               'Did you reboot it?', 'What colour is it?', \
               'You should consider installing anti-virus software.', \
               'Contact Telkom.']
    # use uniform for equal prob vs the randint which is more quassian
    index  = int(uniform(0, 5))
    reply = phrases[index]

    return reply


def main():
    '''main to run this program. prompts user for input and gives random answere'''
    print("Welcome to the automated technical support system. Please describe your problem:")

    isRunning = True
    while isRunning:
        answer = input()

        #if quit, break, else ask new question
        if answer.lower() == 'quit':
            isRunning = False
        else:
            question = select_random_phrase()
            print(question)


if __name__ == '__main__':
    main()
