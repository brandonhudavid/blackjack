from Card import Card

class Deck(set):
    def __init__(self):
        self.createDeck()

    def createDeck(self):
        for i in range(1, 14):
            for suit in ["spades", "diamonds", "hearts", "clubs"]:
                self.add(Card(i, suit))
