from Card import Card
from Card import Bower
from random import shuffle

class Deck:
	"""Create and hold all the playing cards"""
	def __init__(self):
		self.deck = []
		self.fill()
		self.shuffle()
	
	def fill(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		ranks = [9, 10, 11, 12, 13, 14]
		for rank in ranks:
			for suit in suits:
				if rank == 9:
					self.deck.append(Bower(rank, suit))
				else:
					self.deck.append(Card(rank, suit))

	def shuffle(self):
		shuffle(self.deck)

	def display(self):
		for card in self.deck:
			print(card)

	def get_flip(self):
		return self.deck[-1]

	def show_flip(self):
		print("Flip is: {0}".format(self.deck[-1]))
