class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.display = None
        self.__str__()

    def __str__(self):
        if self.display:
            return self.display
        if self.value == 11:
            self.value = 10
            self.display = "J of " + self.suit
        elif self.value == 12:
            self.value = 10
            self.display = "Q of " + self.suit
        elif self.value == 13:
            self.value = 10
            self.display = "K of " + self.suit
        elif self.value == 1:
            self.value = 11
            self.display = "A of " + self.suit
        else:
            self.display = str(self.value) + " of " + self.suit
        return self.display
