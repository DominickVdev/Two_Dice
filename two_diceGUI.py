"""
Program: two_diceGUI.py
Author: Dominick Vera 07/18/2023

GUI- based version of the TWo Dice game which compares random numbers and provides the game's outcome.

NOTE: The file breezypythongui.py MUST be in the same directory as this file for the app to run correctly.

"""

from breezypythongui import EasyFrame
import random
from tkinter.font import Font
#Other imports go here

#Class header
class TwoDiceGUI(EasyFrame):
	# Definition of our class contructor method 
	def __init__(self):
		EasyFrame.__init__(self, title = "Two Dice Game", width = 340, height = 280, resizable = False, background = "seagreen")
		# Add the various components to the window 
		self.addLabel(text = "Two Dice Game", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "seagreen", font = Font(family = "Impact", size = 30))
		self.addLabel(text = "Player's Roll is:", row = 1, column = 0, sticky = "NE", background = "seagreen")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly", sticky = "NW")
		self.addLabel(text = "Computer's Roll is:", row = 2, column = 0, sticky = "NE", background = "seagreen")
		self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1, width = 4, state = "readonly", sticky = "NW")

		# Roll dice button
		self.button = self.addButton(text = "Roll Dice", row = 3, column = 0, columnspan = 2, command = self.roll)


		self.resultArea = self.addLabel(text = "", row = 4, column= 0, columnspan = 2, background = "seagreen", foreground = "yellow", font = Font(family = "Georgia", size = 20), sticky = "NSEW")

	# Roll dice command 
	def roll(self):
		# Variables for this function
		playerDie = random.randint(1, 6)
		compDie = random.randint(1, 6)

		#Processing phase
		if playerDie > compDie:
			result = "Congrats, You've won!"
			self.resultArea["foreground"] = "springgreen"
		elif compDie > playerDie:
			result = "Sorry, you've lost..."
			self.resultArea["foreground"] = "red"
		else:
			result = "You're both Tied"
			self.resultArea["foreground"] = "white"

		# output phase
		self.playerRoll.setNumber(playerDie)
		self.computerRoll.setNumber(compDie)
		self.resultArea["text"] = result

	
# Definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	TwoDiceGUI().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()