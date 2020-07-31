def select_phrase(word):
    ''' selects phrase from dict '''
    phrases = {
        'Crashed':'Are the drivers up to date?',
        'Blue':'Ah, the blue screen of death. And then what happened?',
        'Hacked':'You should consider installing anti-virus software.',
        'Bluetooth':'Have you tried mouthwash?',
        'Apple':'You do mean the computer kind?',
        'Windows':'Ah, I think I see your problem. What version?',
        'Spam':'You should see if your mail client can filter messages.',
        'Connection':'Contact Telkom.',
        ' ':'Curious, tell me more.'
    }

    #None set up for looping through sentense
    answer = phrases.get(word.capitalize(), None)
    return answer


def search(sentence):
    ''' Searches if a word in phrase is connected to  response '''
    words = sentence.split(" ")
    # append a space to the end of list to guarantee termination of loop
    # when all options have been searched and returned unsuccessful. The way
    # this loop is set up, it will exit efficiently withouth another check
    # once first match is found.
    words.append(' ')
    index  = 0
    response = None
    while not response:
        w = words[index]
        response = select_phrase(w)
        index += 1
    return response



def main():
    ''' main '''
    msg = 'Welcome to the automated technical\nPlease describe your problem:'
    isRunning = True

    while isRunning:
        opt = input(msg+'\n')
        if opt.lower() == 'quit':
            isRunning = False
        else:
            #this way response is printed out with input method
            msg = search(opt)
    print("done")

if __name__ == '__main__':
    main()
