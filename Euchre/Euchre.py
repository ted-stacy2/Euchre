from Deck import Deck
from Player import Player
from Game import Game
from Trick import Trick
from Team import Team

class Euchre():
	"""Top-level view of the entire game"""
	def __init__(self):
		self.deck = Deck()
		self.players = []
		self.team1 = Team()
		self.team2 = Team()

	def add_players(self):
		""" Add the 4 players to the game and create teams """
		team1 = True
		names = ["T", "B", "M", "G"]
		for i in range(4):
			#name = input("Player {0}'s name?: ".format(i+1))
			newPlayer = Player(names[i])
			self.players.append(newPlayer)
			if team1:
				self.team1.add_player(newPlayer)
				newPlayer.set_team(1)
				team1 = False
			else:
				self.team2.add_player(newPlayer)
				newPlayer.set_team(2)
				team1 = True

	def start_game(self):
		""" Start the game """
		Game(self.players, self.deck).start()

euchre = Euchre()

# add 4 players
euchre.add_players()

# start the game
euchre.start_game()
