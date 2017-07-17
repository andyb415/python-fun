#-------------------------------------------------------------------------------
# Name:     magnify.py
# Purpose:
# Input:
# Output:
#
# Author:   Andy Bupp -
#
# Created:  06/29/2017 -
# Modified:
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import time
import sys
import curses
import myletters
import os

def enlargeText(ink,paper,userinput):
    #os.system('clear')
    length = len(userinput)
    for i in range(1,8):  # range is 1 through 8 b/c there are 7 rows in each letter
        for j in range(0,length): # range here is 0 through length of word to print
            if j < (length-1):
                try:
                    sys.stdout.write(getattr(myletters, 'magnify_letter_%s' % userinput[j])(i,paper,ink))
                except:
                    sys.stdout.write(myletters.magnify_letter_unknown(i,paper,ink))
            else:
                try:
                    sys.stdout.write(getattr(myletters, 'magnify_letter_%s' % userinput[j])(i,paper,ink)+'\n')
                except:
                    sys.stdout.write(myletters.magnify_letter_unknown(i,paper,ink)+'\n')



    #sys.stdout.flush()
