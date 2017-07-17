#-------------------------------------------------------------------------------
# Name:     hangman.py
# Purpose:  play the game of hangman
# Input:
# Output: enlarged letters to console
#
# Author:   Andy Bupp -
#
# Created:  06/29/2017 -
# Modified:
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import os
import time
import sys
import curses
import random
import math

import magnify
import myletters


#guessedchar = ''
def main():
    fo = open("./hangmanwords.txt", "r")
    win = False
    lines = fo.readlines()
    os.system('clear')
    secret = list(lines[int(math.floor(random.random()*len(lines)))].rstrip('\n'))
    displaymask = list('-'* len(secret))
    badletters = list('')
    guesscounter = 0
    loopflag = True
    magnify.enlargeText(' ','W',''.join(displaymask))
    sys.stdout.write('  \n')
    sys.stdout.write('  \n')
    sys.stdout.write('* * * G U E S S E D  L E T T E R S * * *\n')
    magnify.enlargeText(' ','W',''.join(badletters))
    sys.stdout.write('  \n')
    sys.stdout.write('  \n')
    guessedchar = raw_input('\n guess: ')

    os.system('clear')

    while (guesscounter < 5):

        for i in xrange(len(secret)):
            if secret[i] == guessedchar:
                displaymask[i] = guessedchar

        for i in xrange(len(secret)):
            if not guessedchar in secret:
                if not guessedchar in badletters:
                    badletters.append(guessedchar)
                    guesscounter = guesscounter + 1

        magnify.enlargeText(' ','W',''.join(displaymask))
        sys.stdout.flush()
        sys.stdout.write('  \n')
        sys.stdout.write('  \n')
        sys.stdout.write('* * * G U E S S E D  L E T T E R S * * *\n')
        magnify.enlargeText(' ','W',''.join(badletters))
        sys.stdout.write('  \n')
        sys.stdout.write('  \n')
        if map(str.strip,displaymask) == map(str.strip,secret):
            win = True
            break
        guessedchar = raw_input('\n guess: ')
        os.system('clear')
    if (win):
        magnify.enlargeText(' ','W','you win')
    else:
        magnify.enlargeText(' ','W','you lose')



if __name__ == '__main__':
    main()
