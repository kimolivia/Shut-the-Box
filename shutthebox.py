"""
Olivia Kim
Shut the Box
Last Updated: 12/14/2015
"""

import random

tile = [1,2,3,4,5,6,7,8,9,10,11,12]
    
def printTile(tile):
    """input: tile
        output: none
        prints a fancy version of the tiles
    """
    s ="|-------------------------------------------------|\n"
    for i in range(0,len(tile)):
        s += " " + str(tile[i]) + " |"
    print s[:-1] 
    print "|-------------------------------------------------|"

def box():
    """input: none
        output: allows the user to play the game and returns False if there are no more moves and returns True if you have won the game.
    """
    while True:
        if 1 not in tile and 2 not in tile and 3 not in tile and 4 not in tile and 5 not in tile and 6 not in tile and 7 not in tile and 8 not in tile and 9 not in tile and 10 not in tile and 11 not in tile and 12 not in tile:
            #no numbers left in tiles only x
            print "You win! Your score is: 0!"
            return True
        else:
            print "Welcome player! The dice have rolled you the numbers..."
            dice1 = random.choice(range(1,7))
            dice2 = random.choice(range(1,7))
            print dice1, "&", dice2
            total = dice1 + dice2

            score = 0
            if (dice1 not in tile and dice2 not in tile) and (total not in tile):
                for i in range(0,len(tile)):
                    if tile[i] == 'X':
                        tile[i] = 0
                    score = score + tile[i]
                print "No moves! Your final score is: ", str(score)
                return False

            choicenumbers = []
            printTile(tile)
            print "These are your remaining tiles"
            chosentiles = ""
            while chosentiles not in tile or chosentiles not in [dice1,dice2,total]:
                chosentiles = raw_input("What tiles would you like to put down?")
                if "," not in chosentiles:
                    try:
                        chosentiles = int(chosentiles)
                        choicenumbers = [chosentiles]
                    except ValueError:
                        chosentiles = ""
                else:
                    choicenumbers = []
                    choicenumbers = chosentiles.split(",")
                    try:
                        choicenumbers[0] = int(choicenumbers[0])
                        choicenumbers[1] = int(choicenumbers[1])
                        if sorted(choicenumbers) == sorted([dice1,dice2]) and (choicenumbers[0] in tile and choicenumbers[1] in tile):
                            chosentiles = dice2
                    except ValueError:
                        chosentiles = ""

            else:
                for item in choicenumbers:
                    if item in tile:
                        posit = tile.index(item)
                        tile[posit] = 'X'                      

box()

