'''method that assembles and prints the 'ascii-art' '''
def print_pic():
    # define most used shapes for easy of typing out (spaces not included)
    l_ear = '(\\'
    r_ear = '/)'
    face_1 = "( '')"
    face_2 = '(,, )'
    foot = '(")'
    face_3 = "(\\'.'/)"
    face_4 = '(" )'

    # create F-string to print out. broken up in each line for ease of reading
    pic = F" {l_ear}\\               {l_ear}{r_ear}""\n"
    pic += F" {face_1}    {l_ear}_{r_ear}   {face_2}    /{r_ear}" "\n" "\n"
    pic += F"O{foot}{foot}  {face_3} {foot*2}O  {face_4}" "\n" "\n"
    pic += F"         {foot}_{foot}         ()()o"
    print(pic)


''' main method to run '''
def main():
    print_pic()


if __name__ == '__main__':
    main()
