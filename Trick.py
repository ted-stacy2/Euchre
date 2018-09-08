class Trick:
	""" game-logic behind each Trick """
	def __init__(self, flip, dealer, players, position):
		self.flip = flip
		self.dealer = dealer
		self.players = players
		self.position = position

	def calling_round(self):
		""" Logic behind calling the deal up"""
		inPlay = True
		while inPlay:
			break
