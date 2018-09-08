class Team():
	def __init__(self):
		self.players = []
		self.score = 0

	def __str__(self):
		return "This team contains: {0} and {1}".format(self.players[0].getName(), self.players[1].getName())

	def add_player(self, player):
		self.players.append(player)

	def add_points(self, euchred = False):
		if euchred == True:
			self.score += 2
		else:
			self.score += 1