import re

def to_english(sentence):
    words = sentence.split(" ")
    english_sentence = ''
    english_list = []

    # regex for matching which type of word it is:
    pattern_cons = re.compile(r'(a)([^aeiouAEIOU\d])+(ay)\b')
    pattern_vowl = re.compile(r'(way)\b')

    # loop through words
    for w in words:
        # because pig-latin to english and vice verse are not a 1-1 mapping
        # we cannot make exact translations back into english without extra
        # rules like how 'w' is not in the origial english words we can
        # just search for a string ending in 'way' for an english word
        # starting wit a vowel.
        cons = pattern_cons.search(w)
        vowl = pattern_vowl.search(w)
        english  = ''

        if vowl:
            english = re.sub(pattern_vowl, '', w)
        elif cons:
            suff = cons.group()
            l = len(suff)
            lw = len(w)
            orig = w[:lw-l]
            english = suff[1:l-2]+orig
        else:
            english = w
        english_list.append(english)
    english_sentence = ' '.join(english_list)
    return english_sentence


def to_pig_latin(sentence):

    words = sentence.split(" ")
    latin_sentence = ''
    latin_list = []
    # regex for matching which type of word it is
    pattern_cons = re.compile(r'^([^aeiouAEIOU\d])*')
    pattern_vowl =re.compile(r'^[aeiou]')

    # loop through words;
    for w in words:
        cons = pattern_cons.match(w)
        vowl = pattern_vowl.match(w)
        latin = ''

        if vowl:
            # do the vowel moves
            latin_list.append(w+"way")
        elif cons:
            # do the consonats moves
            pre = cons.group()
            l = len(pre)
            latin_list.append(w[l:]+"a"+pre+"ay")
        else:
            # its a number or symbol, leave as is
            latin_list.append(w)
    latin_sentence = " ".join(latin_list)
    return latin_sentence

def main():
  ''' main '''
  isRunning = True
  while isRunning:
    req = input("(E)nglish or (P)ig Latin or (Q)uit? ")
    if req == 'E':
      text = input("Please enter an English sentence:\n")
      latin = to_pig_latin(text)
      print("\nPig Latin:")
      print(latin)
    elif req == 'P':
      text = input("Please enter a Pig-Latin sentence:\n")
      english = to_english(text)
      print("\nEnglish:")
      print(english)
    elif req == 'Q':
      isRunning = False
    else:
      print("Invalid option")

if __name__ == '__main__':
  main()
