import random

class Person:
    def __init__(self):
        self.hand = []
        self.displayHand = []
        self.value = 0

    def createDisplayHand(self):
        self.displayHand = []
        for card in self.hand:
            self.displayHand.append(str(card))

    def deal(self, deck):
        card = random.choice(tuple(deck))
        deck.remove(card)
        self.hand.append(card)
        self.calculateValue()
        self.createDisplayHand()

    def calculateValue(self):
        self.value = 0
        for card in self.hand:
            self.value += card.value
        if self.value > 21:
            for card in self.hand:
                if card.value == 11:
                    card.value = 1
                    self.calculateValue()
                    break
