from Person import Person

class Player(Person):
    def __init__(self):
        super().__init__()
        self.money = 500.0
        self.bet = 0
    
    def placeBet(self):
        try:
            bet = float(input())
            while bet > self.money or bet <= 0:
                if bet <= 0:
                    print("You must bet a positive amount of money. Place a valid bet.")
                else:
                    print("Bet exceeds your limit of $" + str(player.money) + ". Place a lower bet.")
                bet = float(input())
            self.bet = bet
        except:
            print("Invalid input. Place a numerical bet.")
            self.placeBet()

    def decide(self, deck):
        try:
            decision = input().lower()
            while decision != "deal" and decision != "stand":
                print("Invalid move. Input either deal or stand into the terminal.")
                decision = input().lower()
            if decision == "deal":
                self.deal(deck)
            elif decision == "stand":
                print("Player stands at " + str(self.value) + ".")
                return "STAND"
        except:
            print("Invalid move. Input either deal or stand into the terminal.")
            self.decide(deck)
