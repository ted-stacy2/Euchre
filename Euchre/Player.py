class Player:
	""" Player information and current hand """
	def __init__(self, name):
		self.name = name
		self.hand = []

	def get_name(self):
		return self.name

	def deal_hand(self, deck):
		""" Deals this player 5 cards """
		for _ in range(5):
			self.hand.append(deck.deck.pop())
