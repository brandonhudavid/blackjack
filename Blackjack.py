import sys
import time
from Deck import Deck
from Person import Person
from Player import Player

def main():
    # print intro
    printIntro()
    player = Player()
    dealer = Person()
    while player.money > 0:
        time.sleep(1)
        # start new game
        printNewGame()
        time.sleep(1)
        placeNewBet(player)
        deck = Deck()
        dealInitialHands(player, dealer, deck)
        printDealerHand(dealer, True)
        time.sleep(1)
        # commence player turn
        playerTurn(player, deck)
        if player.value > 21:
            # bust
            playerBust(player)
        elif player.value == 21:
            # blackjack
            playerBlackjack(player)
        elif player.value < 21:
            # commence dealer turn
            dealerTurn(dealer, deck)
            if dealer.value > 21:
                # dealer bust
                dealerBust(dealer, player)
            elif dealer.value == 21:
                # dealer blackjack
                dealerBlackjack(dealer, player)
            elif dealer.value < 21:
                print("Dealer stands.")
                printDealerHand(dealer)
                if dealer.value > player.value:
                    # dealer win
                    dealerWin(player)
                elif dealer.value < player.value:
                    # player win
                    playerWin(player)
                else:
                    print("Tie. You neither gain nor lose money.")
    print("No more money. You lose! Forever! D:")
    time.sleep(1)
    print("Thanks for playing!")
    sys.exit()

def printIntro():
    print("================================")
    print("||   WELCOME TO BLACKJACK!!!  ||")
    print("||        created by          ||")
    print("||       Brandon David        ||")
    print("================================")

def printNewGame():
    print("\n")
    print("================================")
    print("===== STARTING A NEW GAME. =====")
    print("================================")

def placeNewBet(player):
    print("\n")
    print("Place your bet. Amount of money: $" + str(player.money))
    player.placeBet()
    print("=== Wagered bet: $" + str(player.bet) + " ===")
    time.sleep(1)
    print("\n")

def dealInitialHands(player, dealer, deck):
    player.hand = []
    dealer.hand = []
    dealer.deal(deck)
    player.deal(deck)
    dealer.deal(deck)
    player.deal(deck)

def printDealerHand(dealer, hidden=False):
    if hidden:
        print("Dealer's hand:", ["????????", dealer.displayHand[1]])
        print("Dealer's hand value:", "???")
    else:
        print("Dealer's hand:", dealer.displayHand)
        print("Dealer's hand value:", dealer.value)
        
def printPlayerHand(player):
    print("Player's hand:", player.displayHand)
    print("Player's hand value:", player.value)

def playerTurn(player, deck):
    while player.value < 21:
        printPlayerHand(player)
        print("Deal or stand? Input deal or stand into the terminal.")
        if player.decide(deck) == "STAND":
            time.sleep(1)
            break
        time.sleep(1)
        print(str(player.hand[-1]))
        time.sleep(1)
        print("\n")

def dealerTurn(dealer, deck):
    print("================================")
    print("\n")
    print("Dealer's turn.")
    time.sleep(1)
    while dealer.value < 17:
        printDealerHand(dealer)
        time.sleep(1)
        dealer.deal(deck)
        print(str(dealer.hand[-1]))
        time.sleep(1)
        print("\n")

def playerBust(player):
    print("Player's hand:", player.displayHand)
    print("Player's hand value:", player.value)
    print("BUST!!! YOU LOSE!!!")
    player.money -= player.bet
    print("You lost $" + str(player.bet) + ".")

def playerBlackjack(player):
    print("Player's hand:", player.displayHand)
    print("Player's hand value:", player.value)
    print("212121 BLACKJACK!!! YOU WIN!!!")
    player.money += player.bet*1.5
    print("You won $" + str(player.bet*1.5) + ".")

def dealerBust(dealer, player):
    printDealerHand(dealer)
    print("BUST!!! YOU WIN!!!")
    player.money += player.bet
    print("You won $" + str(player.bet) + ".")

def dealerBlackjack(dealer, player):
    printDealerHand(dealer)
    print("212121 BLACKJACK!!! YOU LOSE!!!")
    player.money -= player.bet
    print("You lost $" + str(player.bet) + ".")

def dealerWin(player):
    print("YOU LOSE!!!")
    player.money -= player.bet
    print("You lost $" + str(player.bet) + ".")

def playerWin(player):
    print("YOU WIN!!!")
    player.money += player.bet
    print("You won $" + str(player.bet) + ".")

if __name__ == "__main__":
    main()
