from Trick import Trick
from random import randint

class Game:
	def __init__(self):
		self.dealer = None

	def determine_dealer(self, players):
		self.dealer = players[randint(0, 4)]
