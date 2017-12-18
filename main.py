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
        inPlace=[]
        if player[turn].aces==0:
            player[turn].aces()
            print(alpha[inUse]+': Take \'Aces\' for '+str(player[turn].aces)+' points')
            player[turn].aces=0
            inPlace.append(1)
            inUse+=1
        if player[turn].twos==0:
            player[turn].twos()
            print(alpha[inUse]+': Take \'Twos\' for '+str(player[turn].twos)+' points')
            player[turn].twos=0
            inPlace.append(2)
            inUse+=1
        if player[turn].threes==0:
            player[turn].threes()
            print(alpha[inUse]+': Take \'Threes\' for '+str(player[turn].three)+' points')
            player[turn].threes=0
            inPlace.append(3)
            inUse+=1
        if player[turn].fours==0:
            player[turn].fours()
            print(alpha[inUse]+': Take \'Fours\' for '+str(player[turn].fours)+' points')
            player[turn].fours=0
            inPlace.append(4)
            inUse+=1
        if player[turn].fives==0:
            player[turn].fives()
            print(alpha[inUse]+': Take \'Fives\' for '+str(player[turn].fives)+' points')
            player[turn].fives=0
            inPlace.append(5)
            inUse+=1
        if player[turn].sixes==0:
            player[turn].sixes()
            print(alpha[inUse]+': Take \'Sixes\' for '+str(player[turn].sixes)+' points')
            player[turn].sixes=0
            inPlace.append(6)
            inUse+=1
        if player[turn].fullhouse==0:
            player[turn].fullhouse()
            print(alpha[inUse]+': Take \'Full House\' for '+str(player[turn].fullhouse)+' points')
            player[turn].fullhouse=0
            inPlace.append(7)
            inUse+=1
        if player[turn].smallstraight==0:
            player[turn].smallstraight()
            print(alpha[inUse]+': Take \'Small Straight\' for '+str(player[turn].smallstraight)+' points')
            player[turn].smallstraight=0
            inPlace.append(8)
            inUse+=1
        if player[turn].largestraight==0:
            player[turn].largestraight()
            print(alpha[inUse]+': Take \'Large Straight\' for '+str(player[turn].largestraight)+' points')
            player[turn].largestraight=0
            inPlace.append(9)
            inUse+=1
        if player[turn].threeofakind==0:
            player[turn].threeofakind()
            print(alpha[inUse]+': Take \'Three of a kind\' for '+str(player[turn].threeofakind)+' points')
            player[turn].threeofakind=0
            inPlace.append(10)
            inUse+=1
        if player[turn].fourofakind==0:
            player[turn].fourofakind()
            print(alpha[inUse]+': Take \'Four of a kind\' for '+str(player[turn].fourofakind)+' points')
            player[turn].fourofakind=0
            inPlace.append(11)
            inUse+=1
        if player[turn].yahtzee==0:
            player[turn].yahtzee()
            print(alpha[inUse]+': Take \'Yahtzee\' for '+str(player[turn].yahtzee)+' points')
            player[turn].yahtzee=0
            inPlace.append(12)
            inUse+=1
        if player[turn].chance==0:
            player[turn].chance()
            print(alpha[inUse]+': Take \'Chance\' for '+str(player[turn].chance)+' points')
            player[turn].chance=0
            inPlace.append(13)
            inUse+=1
        pick=input()
        while len(pick)!=1 or not pick.isAlpha():
            print('You must pick exacly one option')
            pick=input()
        if inPlace[alpha.find(pick.upper())]==1:
            player[turn].aces()
        if inPlace[alpha.find(pick.upper())]==2:
            player[turn].twos()
        if inPlace[alpha.find(pick.upper())]==3:
            player[turn].threes()
        if inPlace[alpha.find(pick.upper())]==4:
            player[turn].fours()
        if inPlace[alpha.find(pick.upper())]==5:
            player[turn].fives()
        if inPlace[alpha.find(pick.upper())]==6:
            player[turn].sixes()
        if inPlace[alpha.find(pick.upper())]==7:
            player[turn].fullhouse()
        if inPlace[alpha.find(pick.upper())]==8:
            player[turn].smallstraight()
        if inPlace[alpha.find(pick.upper())]==9:
            player[turn].largestraight()
        if inPlace[alpha.find(pick.upper())]==10:
            player[turn].threeofakind()
        if inPlace[alpha.find(pick.upper())]==11:
            player[turn].fourofakind()
        if inPlace[alpha.find(pick.upper())]==12:
            player[turn].yahtzee()
        if inPlace[alpha.find(pick.upper())]==13:
            player[turn].chance()
        print(names[turn]+'\'s total score is now: '+str(player[turn].aces+player[turn].twos+player[turn].threes+player[turn].fours+player[turn].fives+player[turn].sixes+player[turn].fullhouse+player[turn].smallstraight+player[turn].largestraight+player[turn].threeofakind+player[turn].fourofakind+player[turn].yahtzee+player[turn].chance))
max=0
for turn in range(len(player)):
    if player[turn].aces+player[turn].twos+player[turn].threes+player[turn].fours+player[turn].fives+player[turn].sixes+player[turn].fullhouse+player[turn].smallstraight+player[turn].largestraight+player[turn].threeofakind+player[turn].fourofakind+player[turn].yahtzee+player[turn].chance>max:
        max=player[turn].aces+player[turn].twos+player[turn].threes+player[turn].fours+player[turn].fives+player[turn].sixes+player[turn].fullhouse+player[turn].smallstraight+player[turn].largestraight+player[turn].threeofakind+player[turn].fourofakind+player[turn].yahtzee+player[turn].chance
        topPlayer=turn
print('Congratulations '+names[topPlayer]+'! You won with a score of '+str(max)+'!')