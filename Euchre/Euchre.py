from Deck import Deck
from Player import Player
from Trick import Trick
from Team import Team
from random import randint

class Euchre():
	"""Top-level view of the entire game"""
	def __init__(self):
		self.deck = Deck()
		self.players = []
		self.team1 = Team()
		self.team2 = Team()
		self.dealer = None

	def new_deck(self):
		"""Creates a new deck """
		self.deck = Deck()
		self.position = 0

	def add_players(self):
		""" Add the 4 players to the game and create teams """
		team1 = True
		names = ["Ted", "Tom", "Ben", "Gid"]
		for i in range(4):
			#name = input("Player {0}'s name?: ".format(i+1))
			newPlayer = Player(names[i])
			self.players.append(newPlayer)
			if team1:
				self.team1.add_player(newPlayer)
				team1 = False
			else:
				self.team2.add_player(newPlayer)
				team1 = True

	def deal(self):
		""" deals each player 5 cards"""
		for player in self.players:
			player.deal_hand(self.deck)

	def determine_dealer(self):
		""" Randomly chooses first dealer """
		self.position = randint(0, 3)
		self.dealer = self.players[self.position]

	def show_flip(self):
		""" show top of remainder pile """
		self.flip = self.deck.get_flip()
		self.deck.show_flip()
	
	def start_trick(self):
		""" start the trick """
		args = [self.flip, self.dealer, self.players, self.position]
		self.trick = Trick(*args).calling_round()

	def start_game(self):
		"""  """


euchre = Euchre()

# add 4 players
euchre.add_players()

# start the game
euchre.start_game()


#euchre.determine_dealer()
#euchre.deal()
#euchre.show_flip()
#euchre.start_trick()
