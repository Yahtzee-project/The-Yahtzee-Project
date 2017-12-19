import random
from die import Die
from Yatzee import Scoreboard #?

player=[]
dice=[]
names=[]
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in range(5):
    dice.append(Die())
numPlayers=input('How many players are there? ')
while not numPlayers.isnumeric():
    numPlayers=input('Sorry, I didn\'t get that, how many players? ')
for x in range(int(numPlayers)):
    player.append(Scoreboard()) #set up players
    names.append(input('What\'s your name? '))
for x in range(12):
    for turn in range(len(player)):
        print('Ok '+names[turn]+', your turn now!')
        for y in range(5):
            dice[y].roll()
        diceValues=[dice[0].faceUp,dice[1].faceUp,dice[2].faceUp,dice[3].faceUp,dice[4].faceUp]
        print('You rolled '+str(diceValues[0])+', '+str(diceValues[1])+', '+str(diceValues[2])+', '+str(diceValues[3])+', '+str(diceValues[4]))
        print('Which number dice would you like to reroll?')
        reroll=input()
        if reroll=='quit':
            quit()
        for y in range(len(reroll)):
            if reroll[y].isnumeric():
                dice[int(reroll[y])-1].roll()
        diceValues=[dice[0].faceUp,dice[1].faceUp,dice[2].faceUp,dice[3].faceUp,dice[4].faceUp]
        print('You rolled '+str(diceValues[0])+', '+str(diceValues[1])+', '+str(diceValues[2])+', '+str(diceValues[3])+', '+str(diceValues[4]))
        print('Which number dice would you like to reroll?')
        reroll=input()
        if reroll=='quit':
            quit()
        for y in range(len(reroll)):
            if reroll[y].isnumeric():
                dice[int(reroll[y])-1].roll()
        diceValues=[dice[0].faceUp,dice[1].faceUp,dice[2].faceUp,dice[3].faceUp,dice[4].faceUp]
        print('You rolled '+str(diceValues[0])+', '+str(diceValues[1])+', '+str(diceValues[2])+', '+str(diceValues[3])+', '+str(diceValues[4]))
        print('Which of the following would you like to use?')
        inUse=0
        inPlace=[]
        if player[turn].acesV==-1: #if value hasn't been filled in yet
            player[turn].aces(diceValues) #set the value to what it should be
            print(alpha[inUse]+': Take \'Aces\' for '+str(player[turn].acesV)+' points') #offer the option
            player[turn].acesV=-1 #reset value, in case player doesn't take it
            inPlace.append(1) #set up a list so that code knows where it is in the list
            inUse+=1 #how many have been used yet
        if player[turn].twosV==-1:
            player[turn].twos(diceValues)
            print(alpha[inUse]+': Take \'Twos\' for '+str(player[turn].twosV)+' points')
            player[turn].twosV=-1
            inPlace.append(2)
            inUse+=1
        if player[turn].threesV==-1:
            player[turn].threes(diceValues)
            print(alpha[inUse]+': Take \'Threes\' for '+str(player[turn].threesV)+' points')
            player[turn].threesV=-1
            inPlace.append(3)
            inUse+=1
        if player[turn].foursV==-1:
            player[turn].fours(diceValues)
            print(alpha[inUse]+': Take \'Fours\' for '+str(player[turn].foursV)+' points')
            player[turn].foursV=-1
            inPlace.append(4)
            inUse+=1
        if player[turn].fivesV==-1:
            player[turn].fives(diceValues)
            print(alpha[inUse]+': Take \'Fives\' for '+str(player[turn].fivesV)+' points')
            player[turn].fivesV=0
            inPlace.append(5)
            inUse+=1
        if player[turn].sixesV==-1:
            player[turn].sixes(diceValues)
            print(alpha[inUse]+': Take \'Sixes\' for '+str(player[turn].sixesV)+' points')
            player[turn].sixesV=-1
            inPlace.append(6)
            inUse+=1
        if player[turn].full_houseV==-1:
            player[turn].full_house(diceValues)
            print(alpha[inUse]+': Take \'Full House\' for '+str(player[turn].full_houseV)+' points')
            player[turn].full_houseV=-1
            inPlace.append(7)
            inUse+=1
        if player[turn].small_straightV==-1:
            player[turn].small_straight(diceValues)
            print(alpha[inUse]+': Take \'Small Straight\' for '+str(player[turn].small_straightV)+' points')
            player[turn].small_straightV=-1
            inPlace.append(8)
            inUse+=1
        if player[turn].large_straightV==-1:
            player[turn].large_straight(diceValues)
            print(alpha[inUse]+': Take \'Large Straight\' for '+str(player[turn].large_straightV)+' points')
            player[turn].large_straightV=-1
            inPlace.append(9)
            inUse+=1
        if player[turn].three_of_a_kindV==-1:
            player[turn].three_of_a_kind(diceValues)
            print(alpha[inUse]+': Take \'Three of a kind\' for '+str(player[turn].three_of_a_kindV)+' points')
            player[turn].three_of_a_kindV=-1
            inPlace.append(10)
            inUse+=1
        if player[turn].four_of_a_kindV==-1:
            player[turn].four_of_a_kind(diceValues)
            print(alpha[inUse]+': Take \'Four of a kind\' for '+str(player[turn].four_of_a_kindV)+' points')
            player[turn].four_of_a_kindV=-1
            inPlace.append(11)
            inUse+=1
        if player[turn].YAHTZEEV==-1:
            player[turn].YAHTZEE(diceValues)
            print(alpha[inUse]+': Take \'YAHTZEE\' for '+str(player[turn].YAHTZEEV)+' points')
            player[turn].YAHTZEEV=-1
            inPlace.append(12)
            inUse+=1
        if player[turn].CHANCEV==-1:
            player[turn].CHANCE(diceValues)
            print(alpha[inUse]+': Take \'CHANCE\' for '+str(player[turn].CHANCEV)+' points')
            player[turn].CHANCEV=-1
            inPlace.append(13)
            inUse+=1
        pick=input()
        while len(pick)!=1 or not pick.isalpha():
            print('You must pick exacly one option')
            pick=input()
        if inPlace[alpha.find(pick.upper())]==1:
            player[turn].aces(diceValues)
        if inPlace[alpha.find(pick.upper())]==2:
            player[turn].twos(diceValues)
        if inPlace[alpha.find(pick.upper())]==3:
            player[turn].threes(diceValues)
        if inPlace[alpha.find(pick.upper())]==4:
            player[turn].fours(diceValues)
        if inPlace[alpha.find(pick.upper())]==5:
            player[turn].fives(diceValues)
        if inPlace[alpha.find(pick.upper())]==6:
            player[turn].sixes(diceValues)
        if inPlace[alpha.find(pick.upper())]==7:
            player[turn].full_house(diceValues)
        if inPlace[alpha.find(pick.upper())]==8:
            player[turn].small_straight(diceValues)
        if inPlace[alpha.find(pick.upper())]==9:
            player[turn].large_straight(diceValues)
        if inPlace[alpha.find(pick.upper())]==10:
            player[turn].three_of_a_kind(diceValues)
        if inPlace[alpha.find(pick.upper())]==11:
            player[turn].four_of_a_kind(diceValues)
        if inPlace[alpha.find(pick.upper())]==12:
            player[turn].YAHTZEE(diceValues)
        if inPlace[alpha.find(pick.upper())]==13:
            player[turn].CHANCE(diceValues)
        print(names[turn]+'\'s total score is now: '+str(player[turn].acesV+player[turn].twosV+player[turn].threesV+player[turn].foursV+player[turn].fivesV+player[turn].sixesV+player[turn].full_houseV+player[turn].small_straightV+player[turn].large_straightV+player[turn].three_of_a_kindV+player[turn].four_of_a_kindV+player[turn].YAHTZEEV+player[turn].CHANCEV+11-x))
max=0
for turn in range(len(player)):
    if player[turn].acesV+player[turn].twosV+player[turn].threesV+player[turn].foursV+player[turn].fivesV+player[turn].sixesV+player[turn].full_houseV+player[turn].small_straightV+player[turn].large_straightV+player[turn].three_of_a_kindV+player[turn].four_of_a_kindV+player[turn].YAHTZEEV+player[turn].CHANCEV>max:
        max=player[turn].acesV+player[turn].twosV+player[turn].threesV+player[turn].foursV+player[turn].fivesV+player[turn].sixesV+player[turn].full_houseV+player[turn].small_straightV+player[turn].large_straightV+player[turn].three_of_a_kindV+player[turn].four_of_a_kindV+player[turn].YAHTZEEV+player[turn].CHANCEV
        topPlayer=turn
print('Congratulations '+names[topPlayer]+'! You won with a score of '+str(max)+'!')