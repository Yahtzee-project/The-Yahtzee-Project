import random
from die import die
from scorecard import scorecard #?

player=[]
dice=[]
names=[]
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in range(5):
    dice.append(die())
numPlayers=input('How many players are there? ')
while not numPlayers.isNumeric:
    numPlayers=input('Sorry, I didn\'t get that, how many players? ')
for x in range(int(numPlayers)):
    player.append(scorecard())
    name.append(input('What\'s your name? '))
for x in range(13):
    for turn in range(len(player)):
        print('Ok '+name[turn]+', your turn now!')
        for y in range(5):
            dice[y].roll()
        print('You rolled '+dice[0]+', '+dice[1]+', '+dice[2]+', '+dice[3]+', '+dice[4])
        print('Which number dice would you like to reroll?')
        reroll=input()
        for y in range(len(reroll)):
            if reroll[y].isNumeric():
                dice[y].roll()
        print('You rolled '+dice[0]+', '+dice[1]+', '+dice[2]+', '+dice[3]+', '+dice[4])
        print('Which number dice would you like to reroll?')
        reroll=input()
        for y in range(len(reroll)):
            if reroll[y].isNumeric():
                dice[y].roll()
        diceValues=[dice[0].faceUp,dice[1].faceUp,dice[2].faceUp,dice[3].faceUp,dice[4].faceUp]
        print('Which of the following would you like to use?')
        inUse=0
        if scorecard[turn].aces==0:
            scorecard[turn].aces()
            print(alpha[inUse]+': Take \'Aces\' for '+str(scorecard[turn].aces)+' points')
            scorecard[turn].aces=0
        if scorecard[turn].twos==0:
            scorecard[turn].twos()
            print(alpha[inUse]+': Take \'Twos\' for '+str(scorecard[turn].twos)+' points')
            scorecard[turn].twos=0
        if scorecard[turn].threes==0:
            scorecard[turn].threes()
            print(alpha[inUse]+': Take \'Threes\' for '+str(scorecard[turn].three)+' points')
            scorecard[turn].threes=0
        if scorecard[turn].fours==0:
            scorecard[turn].fours()
            print(alpha[inUse]+': Take \'Fours\' for '+str(scorecard[turn].fours)+' points')
            scorecard[turn].fours=0
        if scorecard[turn].fives==0:
            scorecard[turn].fives()
            print(alpha[inUse]+': Take \'Fives\' for '+str(scorecard[turn].fives)+' points')
            scorecard[turn].fives=0
        if scorecard[turn].sixes==0:
            scorecard[turn].sixes()
            print(alpha[inUse]+': Take \'Sixes\' for '+str(scorecard[turn].sixes)+' points')
            scorecard[turn].sixes=0
        if scorecard[turn].fullhouse==0:
            scorecard[turn].fullhouse()
            print(alpha[inUse]+': Take \'Full House\' for '+str(scorecard[turn].fullhouse)+' points')
            scorecard[turn].fullhouse=0
        if scorecard[turn].smallstraight==0:
            scorecard[turn].smallstraight()
            print(alpha[inUse]+': Take \'Small Straight\' for '+str(scorecard[turn].smallstraight)+' points')
            scorecard[turn].smallstraight=0
        if scorecard[turn].largestraight==0:
            scorecard[turn].largestraight()
            print(alpha[inUse]+': Take \'Large Straight\' for '+str(scorecard[turn].largestraight)+' points')
            scorecard[turn].largestraight=0
        if scorecard[turn].threeofakind==0:
            scorecard[turn].threeofakind()
            print(alpha[inUse]+': Take \'Three of a kind\' for '+str(scorecard[turn].threeofakind)+' points')
            scorecard[turn].threeofakind=0
        if scorecard[turn].fourofakind==0:
            scorecard[turn].fourofakind()
            print(alpha[inUse]+': Take \'Four of a kind\' for '+str(scorecard[turn].fourofakind)+' points')
            scorecard[turn].fourofakind=0
        if scorecard[turn].yahtzee==0:
            scorecard[turn].yahtzee()
            print(alpha[inUse]+': Take \'Yahtzee\' for '+str(scorecard[turn].yahtzee)+' points')
            scorecard[turn].yahtzee=0
        if scorecard[turn].chance==0:
            scorecard[turn].chance()
            print(alpha[inUse]+': Take \'Chance\' for '+str(scorecard[turn].chance)+' points')
            scorecard[turn].chance=0