def select_phrase(word):
    ''' selects phrase from dict '''
    phrases = {
        'Crashed':'Are the drivers up to date',
        'Blue':'Ah, the blue screen of death. And then what happened?',
        'Hacked':'You should consider installing anti-virus software.',
        'Bluetooth':'Have you tried mouthwash?',
        'Apple':'You do mean the computer kind?',
        'Windows':'Ah, I think I see your problem. What version?',
        'Spam':'You should see if your mail client can filter messages.',
        'Connection':'Contact Telkom.'
    }

    answer = phrases.get(word.capitalize(), 'Curious, tell me more.')
    return answer


def main():
    ''' main '''
    msg = 'Welcome to the automated technical\nPlease describe your problem:'
    isRunning = True

    while isRunning:
        opt = input(msg+'\n')
        if opt.lower() == 'quit':
            isRunning = False
        else:
            msg = select_phrase(opt)
    print("done")


if __name__ == '__main__':
    main()
