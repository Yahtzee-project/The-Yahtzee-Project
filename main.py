player=[]
dice=[]
names=[]
for x in range(5):
    dice.append(die())
numPlayers=input('How many players are there? ')
while not numPlayers.isNumeric:
    numPlayers=input('Sorry, I didn\'t get that, how many players? ')
for x in range(int(numPlayers)):
    player.append(scorecard())
    name.append(input('What\'s your name? '))