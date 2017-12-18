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

    def twos():
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

    def threes():
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

    def fours():
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

	def fives():
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

    	self.fives = points

	def sixes():
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

    	self.sixes = points

	def three_of_a_kind(): #check
		points = 0
		points = int(dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5])

		self.three_of_a_kind = points

	def four_of_a_kind(): #check
		points = 0
		points = int(dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5])

		self.four_of_a_kind = points

	def full_house(): #check
		points = 0
		points = points + 25

		self.full_house = points

	def small_straight(): #check
		points = 0
		points = points + 30

		self.small_straight = points

	def large_straight(): #check
		points = 0
		points = points + 40

		self.large_straight = points

	def YAHTZEE(): #check
		points = 0
		if dice[0] = dice[1] = dice[2] = dice[3] = dice[4] = dice[5]:
			points = points + 50

		self.YAHTZEE = points

	def CHANCE():
		points = 0
		points = int(dice[0] + dice[1] + dice[2] + dice[3] + dice[4] + dice[5])

		self.CHANCE = points
