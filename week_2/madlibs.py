import random
adjective = ['']*6
noun = ['']*6
plural = ['']*6
female = ['']*6
clothes = ['']*6
city = ['']*6
body_part = ['']*6
alphabet = ['']*6
place = ['']*6
celeb = ['']*6
verb = ['']*6
number = ['']*6
dict = {'adjective':adjective, 'noun':noun, 'plural noun':plural, \
        'female name':female, 'city':city, 'body part':body_part, \
        'letter':alphabet, 'place':place, 'celeb':celeb, 'verb':verb, \
        'number':number, 'clothes':clothes}


def populate():
    global dict
    #loop through each entry in dict and get 6 of each
    keys = dict.keys()
    for k in keys:
        #l = dict[k]
        for i in range(6):
            msg = F"please enter a {k} ({(6-i)} remaining): "
            x = input(msg)
            dict[k][i] = x
        #dict[k] = l


def test_dict():
    global dict
    print(dict)


def get_word(word):
    global dict
    output = ''
    index = 0
    item = []
    #since we are using random indices, only continue when valid random unique word is found.
    while (output == ''):
        index = random.randint(0,5)
        item = dict[word];
        output = item[index]
    #delete word as to not allow duplicates
    item[index] = ''
    dict[word] = item
    return output


def print_madlib():
    #Using F-strings we can build up our madlib and use a function to give us
    #the randomly selected word. F-strings are simpler than .format().
    msg = F"There are many { get_word('adjective') } ways to choose a/an "
    msg += F"{get_word('noun')} to read." "\n"
    msg += F"First, you could ask for recommendations from your friends "
    msg += (F"and {get_word('plural noun')}." "\n")
    msg += F"Just dont ask Aunt {get_word('female name')} - she only reads "
    msg += F"{get_word('adjective')} books with {get_word('clothes')}-ripping "
    msg += (F"goddesses on the cover." "\n")
    msg += F"If your friends and family are no help, try checking out "
    msg += F"the {get_word('noun')} Review in The {get_word('city')} Times." "\n"
    msg += F"If the {get_word('plural noun')} featured there are too "
    msg += F"{get_word('adjective')} for your taste, try something a little more "
    msg += (F"low-{get_word('body part')}, like {get_word('letter')}." "\n")
    msg += (F"The {get_word('celeb')} Magazine-fashioned way." "\n")
    msg += F"Head to your local library or {get_word('place')} and browse the shelves until "
    msg += (F"something catches your {get_word('body part')}." "\n")
    msg += F"Or, you could save yourself a whole lot of {get_word('adjective')} "
    msg += F"trouble and log on to www.bookish.com, the {get_word('adjective')} "
    msg += F"new website to {get_word('verb')} for books! With all the time "
    msg += F"you'll save not having to search for {get_word('plural noun')}, "
    msg += (F"you can read {get_word('number')} more books!" "\n")


def main():
    populate()
    test_dict()
    print_madlib()


if __name__ == '__main__':
    main()
