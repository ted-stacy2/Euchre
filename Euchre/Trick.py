class Trick:
	""" game-logic behind each Trick """
	def __init__(self, flip, dealer, players, position):
		self.flip = flip
		self.dealer = dealer	 	# Player that is dealer
		self.players = players
		self.position = position 	# Position of the dealer
		self.score = [0, 0]
		self.trump = ""				# trump suit for this trick
		self.called = 0				# which team called up the hand

	def start(self):
		""" Starts the trick """
		self.trump = self.calling_round()
		print("{0} is trump.".format(self.trump))
		print("Team {0} called it up.".format(self.called))
		self.play()

	def calling_round(self):
		""" 
		Logic behind calling/passing the deal
		return: suit that is trump 
		"""
		calling = True					# true until picked up or dealer turned down
		flipped = False					# false until dealer turns down card
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]	# Available suits, one is removed if card is flipped

		if self.position != 3:
			current_position = self.position + 1
		else:
			current_position = 0

		# first round of calls, determine if the dealer will pick up the card
		# or will it be flipped and move to the second round
		while calling:
			# decision tree for non-dealers
			print("{0}'s turn.".format(self.players[current_position].get_name()))
			if current_position != self.position:
				call = input("Would you like to order it up?(y/n): ")
				if call == "y" or call == "Y":
					self.dealer.pick_it_up(self.flip)
					self.called = self.players[self.position].get_team()
					return self.flip.get_suit()
				else:
					if current_position != 3:
						current_position += 1
					else:
						current_position = 0
					continue
			# decision tree for the dealer
			else:
				call = input("Would you like to pick it up?(y/n): ")
				if call == "y" or call == "Y":
					self.dealer.pick_it_up(self.flip)
					self.called = self.players[self.position].get_team()
					return self.flip.get_suit()
				else:
					if current_position != 3:
						current_position += 1
					else:
						current_position = 0
				calling = False
				flipped = True

		# players are not allowed to call suit of flipped card
		unavailable_suit = self.flip.get_suit()
		suits.remove(unavailable_suit)

		# the card has been flipped so now the players must decide what suit
		# they want to call, if it gets to the dealer, s/he must make a call
		while flipped:
			print("{0}'s turn.".format(self.players[current_position].get_name()))
			# non-dealer decisions
			if current_position != self.position:
				call = input("What would you like to call?({0}, {1}, {2} or n): " \
					.format(suits[0], suits[1], suits[2]))
				if call in suits:
					self.called = self.players[self.position].get_team()
					return call
				else:
					if current_position != 3:
						current_position += 1
					else:
						current_position = 0
					continue
			# dealers call, must make a decision
			else:
				call = input("Screw the dealer, you must call a suit:({0}, {1}, {2}): " \
					.format(suits[0], suits[1], suits[2]))
				if call not in suits:
					print("Not a valid suit. Please try again.")
					continue
				else:
					self.called = self.players[self.position].get_team()
					return call

	def play(self):
		""" Trump has been decided, now start playing """

		# determine who leads
		if self.position != 3:
			lead = self.position + 1
		else:
			lead = 0

		# for now, play all 5 hands
		# TODO: if getting euchred, only play enough of the hand to know its over

		for _ in range(5):
			card = self.players[lead].lead()
			suit = card.get_suit()
			played_cards = [card]
			for _ in range(3):
				if lead != 3:
					lead += 1
				else:
					lead = 0
				card = self.players[lead].follow_suit(suit)
				played_cards.append(card)
