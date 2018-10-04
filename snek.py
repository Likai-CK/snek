# SNEK

from time import sleep
from random import randint
from colorama import init
init()

space_count = 0
direction = "right"
left = "\\ \\"
center = "|"
right = "/ /"
spaces = ""
loops = 0
#snek = True
randforecolor = 0
randbackcolor = 0
Fore_RED = '\033[31m'
Fore_BLUE = '\033[34m'
Fore_GREEN = '\033[32m'
Fore_YELLOW = '\033[33m'
Fore_MAGENTA = '\033[35m'
Fore_CYAN = '\033[36m'
Fore_WHITE = '\033[37m'

forecolors = [Fore_RED, Fore_BLUE, Fore_GREEN, Fore_YELLOW, Fore_MAGENTA, Fore_CYAN, Fore_WHITE]
#backcolors = [Back_RED, Back_BLUE, Back_GREEN, Back_YELLOW, Back_MAGENTA, Back_CYAN, Back_WHITE]
rightmax = 25
leftmax = 1
changedirection = randint(1, 50)


def print_spaces(n, return_value):
    returnstring = ""
    count = n
    while count > 1:
        returnstring = returnstring + " "
        count += -1
    return returnstring
        
#print print_spaces(5, "")
while True:
    #changedirection = randint(1, 125)
    
    if loops > changedirection:
        rightmax = randint(leftmax+2, 55)
        leftmax = randint(1,rightmax-2)
        randforecolor = randint(0, len(forecolors) - 1)
        loops = 0
        changedirection = randint(1, 50)

        
    if(space_count >= rightmax):
        direction = "left"
    if(space_count < leftmax):
        direction = "right"
        
        
    if(direction == "right"):
        space_count += 1
        spaces = print_spaces(space_count, " ")
        if( space_count == (rightmax / 2) + 1):
            print(forecolors[randforecolor] +  spaces + "S " + right[0])
        elif( space_count == (rightmax / 2) + 2):
            print(forecolors[randforecolor] +  spaces + "N " + right[0])
        elif( space_count == (rightmax / 2) + 3):
            print(forecolors[randforecolor] + spaces + "E " + right[0])
        elif( space_count == (rightmax / 2) + 4):
            print(forecolors[randforecolor] + spaces + "K " + right[0])
        else:
 
            print(forecolors[randforecolor] +  spaces + right)
    else:
        space_count += -1
        spaces = print_spaces(space_count, " ")
        print(forecolors[randforecolor] + spaces + left)
        
    sleep(0.035)
    loops += 1
   # print('\033[30m') # resets style to default color
        