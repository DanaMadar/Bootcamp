import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
vals = ['A', '2', '3', '4', '5', '6', '7',
        '8', '9', '10', 'J', 'Queen Dana', 'K']


class Card:
    def __init__(self, suits, val):
        self.suits = suits
        self.vals = val

    def __repr__(self):
        return f'{self.vals} of {self.suits}'


class Deck():
    def __init__(self):
        self.deck = []

    def shuffle(self):
        for suit in suits:
            for val in vals:
                self.deck.append(Card(suit, val))
        if len(self.deck) == 52:
            random.shuffle(self.deck)

    def deal(self):
        new_card = random.choice(self.deck)
        self.deck.remove(new_card)
        return new_card


deck = Deck()
deck.shuffle()
print(deck.deal())
