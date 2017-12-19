# The-Yahtzee-Project

In this repository, there is a Yahtzee Game!

Project by Jonathan Geller and Rohin Shivdasani

Sources:
http://www.thegeekstuff.com/2013/06/python-list/?utm_source=feedly
https://wiki.python.org/moin/HowTo/Sorting
http://www.diveintopython.net/file_handling/for_loops.html
(Andy Si and Mitchell Jones helped minimally helped Rohin one night with some things in the Scorecard Class)

On my honor, I have niether given nor recieved unauthorized aid on this assignment. 


pic = (https://cardgames.io/yahtzee/images/yahtzee-logo.png)







Class Scorecard

different variables for each category on the Yahtzee board

ex. self.twos=-1, when player fills it in, set it to the value

different functions for each category on the board

ex. twos(self) sets self.twos to 2*number of twos showing on the dice

(-1 to be able to differentiate between boxes that haven't been filled in yet and boxes that have been filled in with zero)

Class Die

self.value=1

roll(self) sets self.value to a random integer between 1 and 6

sum(self) returns total point value of scorecard

scorecards will be held in a list so that the users can specify the number of players in the game.
