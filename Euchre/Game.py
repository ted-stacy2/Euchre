from Trick import Trick
from random import randint

class Game:
	def __init__(self, players, deck):
		self.dealer = None
		self.players = players
		self.deck = deck
		self.flip = None
		self.position = -1
		self.score = [0, 0]

	def start(self):
		""" Start and run the game """
		self.determine_dealer()
		self.deal()
		self.show_flip()
		#while self.score[0] < 10 and self.score[1] < 10:
		Trick(self.flip, self.dealer, self.players, self.position).start()

	def determine_dealer(self):
		""" Randomly select first dealer """
		self.position = randint(0, 3)
		self.dealer = self.players[self.position]

	def deal(self):
		""" deals each player 5 cards"""
		for player in self.players:
			player.deal_hand(self.deck)
			print("{0}'s hand is: {1}" \
				  .format(player.get_name(), player.get_hand()))

	def show_flip(self):
		""" show top of remainder pile """
		self.flip = self.deck.get_flip()
		self.deck.show_flip()