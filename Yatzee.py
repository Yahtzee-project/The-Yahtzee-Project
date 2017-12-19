class scoreboard:
    def __init__(self):
        self.aces = -1
        self.twos = -1
        self.threes = -1
        self.fours = -1
        self.fives = -1
        self.sixes = -1
        self.three_of_a_kind = -1
        self.four_of_a_kind = -1
        self.full_house = -1
        self.small_straight = -1
        self.large_straight = -1
        self.YAHTZEE = -1
        self.CHANCE = -1
    def aces(self, dice):
        points = 0
        if dice[0] == 1:
            points = points+1
        if dice[1] == 1:
            points = points+1
        if dice[2] == 1:
            points = points+1
        if dice[3] == 1:
            points = points+1
        if dice[4] == 1:
            points = points+1
        self.aces = points
    def twos(self, dice):
        points = 0
        if dice[0] == 2:
            points = points+2
        if dice[1] == 2:
            points = points+2
        if dice[2] == 2:
            points = points+2
        if dice[3] == 2:
            points = points+2
        if dice[4] == 2:
            points = points+2
        self.twos = points
    def threes(self, dice):
        points = 0
        if dice[0] == 3:
            points = points+3
        if dice[1] == 3:
            points = points+3
        if dice[2] == 3:
            points = points+3
        if dice[3] == 3:
            points = points+3
        if dice[4] == 3:
            points = points+3
        self.threes = points
    def fours(self, dice):
        points = 0
        if dice[0] == 4:
            points = points+4
        if dice[1] == 4:
            points = points+4
        if dice[2] == 4:
            points = points+4
        if dice[3] == 4:
            points = points+4
        if dice[4] == 4:
            points = points+4
        self.fours = points
    def fives(self, dice):
        points = 0
        if dice[0] == 5:
            points = points+5
        if dice[1] == 5:
            points = points+5
        if dice[2] == 5:
            points = points+5
        if dice[3] == 5:
            points = points+5
        if dice[4] == 5:
            points = points+5
        self.aces = points
    def sixes(self, dice):
        points = 0
        if dice[0] == 6:
            points = points+6
        if dice[1] == 6:
            points = points+6
        if dice[2] == 6:
            points = points+6
        if dice[3] == 6:
            points = points+6
        if dice[4] == 6:
            points = points+6
        self.aces = points
    def three_of_a_kind(self, dice):
        points = 0
        for i in range(0,3):
            track = 0
            for k in range(i+1,5):
                if dice[i]==dice[k]:
                    track+=1
                if j==2:
                    points = int(dice[0] + dice[1] + dice[2] + dice[3] + dice[4])
        self.three_of_a_kind = points
    def four_of_a_kind(self, dice):
        points = 0
        for i in range(0,2):
            track = 0
            for k in range(i+1,5):
                if dice[i]==dice[k]:
                    track+=1
                if j==3:
                    points = int(dice[0] + dice[1] + dice[2] + dice[3] + dice[4])
        self.four_of_a_kind = points
    def full_house(self, dice):
        points=0
        newDice=dice
        twoDone=False
        threeDone=False
        for x in range(len(newDice)):
            for y in range(x+1,len(newDice)):
                if newDice[x]==newDice[y]:
                    Num1=newDice[x]
                    newDice.pop(x)
                    newDice.pop(y)
                    twoDone=True
                    break
        if twoDone and ((newDice[1]==newDice[2] and newDice[0]==Num1) or (newDice[0]==newDice[2] and newDice[1]==Num1) or (newDice[1]==newDice[0] and newDice[2]==Num1) or (newDice[0]==newDice[1] and newDice[1]==newDice[2])):
            points==25
    def small_straight(self, dice):
        points = 0
        q=False
        newDice=dice
        for x in range(len(newDice)):
            if newDice[x]==1:
                a=True
        for x in range(len(newDice)):
            if newDice[x]==2:
                b=True
        for x in range(len(newDice)):
            if newDice[x]==3:
                c=True
        for x in range(len(newDice)):
            if newDice[x]==4:
                d=True
        for x in range(len(newDice)):
            if newDice[x]==5:
                e=True
        for x in range(len(newDice)):
            if newDice[x]==6:
                f=True       
        if (a and b and c and d) or (e and b and c and d) or (e and f and c and d):
            points = points + 30
        self.small_straight = points
    def large_straight(): #check
        points = 0
        q=False
        newDice=dice
        for x in range(len(newDice)):
            if newDice[x]==1:
                a=True
        for x in range(len(newDice)):
            if newDice[x]==2:
                b=True
        for x in range(len(newDice)):
            if newDice[x]==3:
                c=True
        for x in range(len(newDice)):
            if newDice[x]==4:
                d=True
        for x in range(len(newDice)):
            if newDice[x]==5:
                e=True
        for x in range(len(newDice)):
            if newDice[x]==6:
                f=True       
        if (a and b and c and d and e) or (f and e and b and c and d):
            points = points + 40
    def YAHTZEE():
        points = 0
        if dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]:
            points = points + 50
        self.YAHTZEE = points
    def CHANCE():
        points = 0
        points = int(dice[0] + dice[1] + dice[2] + dice[3] + dice[4])
        self.CHANCE = points
	
		
		
		
