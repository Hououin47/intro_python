import re

def get_input(message):
    ''' Prompts the user for specified input and returns list of words'''
    words = []
    text = input(message)
    # avoid issues with case sensitivity.
    text = text.lower()
    # catch errors like many commas or spaces and with a single space.
    # so both strings each word will only be separated by a single
    # space and splitting is easy
    text = re.sub('(,+)?( +)', ' ', text).strip()
    words = text.split(" ")

    return words


def create_acronym(text, exclude):
    ''' Creates an acronym of  given text, exluding specified words'''
    acronym = ''
    for word in text:
        if word not in exclude:
            w = word[:1]
            acronym += w.upper()
    return acronym


def main():
    ''' main sets up program to do what you want '''
    exclude_list = get_input('Enter words to be ignored separated by commas:\n')
    text = get_input('Enter a title to generate its acronym:\n')

    acronym = create_acronym(text, exclude_list)
    print(acronym)


if __name__ == '__main__':
    main()
