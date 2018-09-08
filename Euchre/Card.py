class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.value = rank - 8

	def get_rank(self):
		return self.rank

	def get_suit(self):
		return self.suit

	def get_value(self):
		return self.value

	def __str__(self):
		return "The {0} of {1}".format(print_rank(self.rank), self.suit)

	def __repr__(self):
		if self.rank == 11:
			rank = 'Jack'
		elif self.rank == 12:
			rank = 'Queen'
		elif self.rank == 13:
			rank = 'King'
		elif self.rank == 14:
			rank = 'Ace'
		else:
			rank = self.rank
			
		return "The {0} of {1}".format(rank, self.suit)


def print_rank(rank):
	if rank == 11:
		rank = 'Jack'
	elif rank == 12:
		rank = 'Queen'
	elif rank == 13:
		rank = 'King'
	elif rank == 14:
		rank = 'Ace'
	else:
		pass
	return rank
