import random
from die import die
from Yahtzee import scoreboard #?

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
    player.append(scoreboard())
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
                dice[reroll[y]].roll()
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
        if player[turn].aces==-1:
            player[turn].aces(dice)
            print(alpha[inUse]+': Take \'Aces\' for '+str(player[turn].aces)+' points')
            player[turn].aces=-1
            inPlace.append(1)
            inUse+=1
        if player[turn].twos==-1:
            player[turn].twos(dice)
            print(alpha[inUse]+': Take \'Twos\' for '+str(player[turn].twos)+' points')
            player[turn].twos=-1
            inPlace.append(2)
            inUse+=1
        if player[turn].threes==-1:
            player[turn].threes(dice)
            print(alpha[inUse]+': Take \'Threes\' for '+str(player[turn].three)+' points')
            player[turn].threes=-1
            inPlace.append(3)
            inUse+=1
        if player[turn].fours==-1:
            player[turn].fours(dice)
            print(alpha[inUse]+': Take \'Fours\' for '+str(player[turn].fours)+' points')
            player[turn].fours=-1
            inPlace.append(4)
            inUse+=1
        if player[turn].fives==-1:
            player[turn].fives(dice)
            print(alpha[inUse]+': Take \'Fives\' for '+str(player[turn].fives)+' points')
            player[turn].fives=0
            inPlace.append(5)
            inUse+=1
        if player[turn].sixes==-1:
            player[turn].sixes(dice)
            print(alpha[inUse]+': Take \'Sixes\' for '+str(player[turn].sixes)+' points')
            player[turn].sixes=-1
            inPlace.append(6)
            inUse+=1
        if player[turn].full_house==-1:
            player[turn].full_house(dice)
            print(alpha[inUse]+': Take \'Full House\' for '+str(player[turn].full_house)+' points')
            player[turn].full_house=0
            inPlace.append(7)
            inUse+=1
        if player[turn].small_straight==0:
            player[turn].small_straight(dice)
            print(alpha[inUse]+': Take \'Small Straight\' for '+str(player[turn].small_straight)+' points')
            player[turn].small_straight=0
            inPlace.append(8)
            inUse+=1
        if player[turn].large_straight==0:
            player[turn].large_straight(dice)
            print(alpha[inUse]+': Take \'Large Straight\' for '+str(player[turn].large_straight)+' points')
            player[turn].large_straight=0
            inPlace.append(9)
            inUse+=1
        if player[turn].three_of_a_kind==0:
            player[turn].three_of_a_kind(dice)
            print(alpha[inUse]+': Take \'Three of a kind\' for '+str(player[turn].three_of_a_kind)+' points')
            player[turn].three_of_a_kind=0
            inPlace.append(10)
            inUse+=1
        if player[turn].four_of_a_kind==0:
            player[turn].four_of_a_kind(dice)
            print(alpha[inUse]+': Take \'Four of a kind\' for '+str(player[turn].four_of_a_kind)+' points')
            player[turn].four_of_a_kind=0
            inPlace.append(11)
            inUse+=1
        if player[turn].YAHTZEE==0:
            player[turn].YAHTZEE(dice)
            print(alpha[inUse]+': Take \'YAHTZEE\' for '+str(player[turn].YAHTZEE)+' points')
            player[turn].YAHTZEE=0
            inPlace.append(12)
            inUse+=1
        if player[turn].CHANCE==0:
            player[turn].CHANCE(dice)
            print(alpha[inUse]+': Take \'CHANCE\' for '+str(player[turn].CHANCE)+' points')
            player[turn].CHANCE=0
            inPlace.append(13)
            inUse+=1
        pick=input()
        while len(pick)!=1 or not pick.isAlpha():
            print('You must pick exacly one option')
            pick=input()
        if inPlace[alpha.find(pick.upper())]==1:
            player[turn].aces(dice)
        if inPlace[alpha.find(pick.upper())]==2:
            player[turn].twos(dice)
        if inPlace[alpha.find(pick.upper())]==3:
            player[turn].threes(dice)
        if inPlace[alpha.find(pick.upper())]==4:
            player[turn].fours(dice)
        if inPlace[alpha.find(pick.upper())]==5:
            player[turn].fives(dice)
        if inPlace[alpha.find(pick.upper())]==6:
            player[turn].sixes(dice)
        if inPlace[alpha.find(pick.upper())]==7:
            player[turn].full_house(dice)
        if inPlace[alpha.find(pick.upper())]==8:
            player[turn].small_straight(dice)
        if inPlace[alpha.find(pick.upper())]==9:
            player[turn].large_straight(dice)
        if inPlace[alpha.find(pick.upper())]==10:
            player[turn].three_of_a_kind(dice)
        if inPlace[alpha.find(pick.upper())]==11:
            player[turn].four_of_a_kind(dice)
        if inPlace[alpha.find(pick.upper())]==12:
            player[turn].YAHTZEE(dice)
        if inPlace[alpha.find(pick.upper())]==13:
            player[turn].CHANCE(dice)
        print(names[turn]+'\'s total score is now: '+str(player[turn].aces+player[turn].twos+player[turn].threes+player[turn].fours+player[turn].fives+player[turn].sixes+player[turn].full_house+player[turn].small_straight+player[turn].large_straight+player[turn].three_of_a_kind+player[turn].four_of_a_kind+player[turn].YAHTZEE+player[turn].CHANCE))
max=0
for turn in range(len(player)):
    if player[turn].aces+player[turn].twos+player[turn].threes+player[turn].fours+player[turn].fives+player[turn].sixes+player[turn].full_house+player[turn].small_straight+player[turn].large_straight+player[turn].three_of_a_kind+player[turn].four_of_a_kind+player[turn].YAHTZEE+player[turn].CHANCE>max:
        max=player[turn].aces+player[turn].twos+player[turn].threes+player[turn].fours+player[turn].fives+player[turn].sixes+player[turn].full_house+player[turn].small_straight+player[turn].large_straight+player[turn].three_of_a_kind+player[turn].four_of_a_kind+player[turn].YAHTZEE+player[turn].CHANCE
        topPlayer=turn
print('Congratulations '+names[topPlayer]+'! You won with a score of '+str(max)+'!')