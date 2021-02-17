class Card:

	def __init__(self,suits,values):
		self.suits = suits
		self.values = values

	def __repr__(self):
		return f'{self.values} of {self.suits}'

class Deck:

	def __init__(self):

		suits = ["Hearts", "Diamond", "Clubs", "Spade"]
		values = ["A", "2", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]

		self.cards = [Card(value,suit) for suit in suits for value in values]
		print(self.cards)

Deck()
#c = Card("A", "Hearts")
#c2 = Card("10", "Diamond")
#c3 = Card("K","Spade")
#print(c)
#print(c2)
#print(c3)



