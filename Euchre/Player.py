class Player:
	""" Player information and current hand """
	def __init__(self, name):
		self.name = name
		self.hand = []
		self.team = 0

	def get_name(self):
		return self.name

	def get_hand(self):
		return self.hand

	def get_team(self):
		return self.team
	def set_team(self, num):
		self.team = num

	def deal_hand(self, deck):
		""" Deals this player 5 cards """
		for _ in range(5):
			self.hand.append(deck.deck.pop())

	def lead(self):
		""" first card played, can be any suit """
		print(self.hand)
		num = int(input("{0} turn, play a card(1-5): ".format(self.name)))
		return self.hand.pop(num-1)

	def follow_suit(self, suit):
		""" 
		This function is for players that are after the dealer
		Check if they have to follow suit
		"""
		has_suit = False
		legal_plays = []
		for card in self.hand:
			if card.get_suit() == suit:
				has_suit = True
				legal_plays.append(card)
		print(self.hand)
		if not has_suit:
			num = int(input("{0}'s turn, play a card(1-{1}): "\
					  .format(self.name, len(self.hand))))
			return self.hand.pop(num-1)
		else:
			while True:
				num = int(input("{0}'s turn, play a card(1-{1}): "\
						  .format(self.name, len(self.hand))))
				if self.hand[num-1] in legal_plays:
					return self.hand.pop(num-1)
				else:
					print("Not a valid play. Please try again.")
					continue

	def pick_it_up(self, flip):
		""" logic behind the dealer dropping a card """
		print(self.hand)
		drop = int(input("{0} must drop a card(1-5): ".format(self.name)))
		self.hand.pop(drop-1)
		self.hand.append(flip)
		print(self.hand)
