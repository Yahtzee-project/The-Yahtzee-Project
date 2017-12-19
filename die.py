import random
class Die:
    def __init__(self):
        self.faceUp=1
    def roll(self):
        self.faceUp=random.randint(1,6)
        