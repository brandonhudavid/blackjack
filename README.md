# Blackjack
Design document: https://docs.google.com/document/d/1yJSovIVAnl4-7PgV6dx4yUBWJgEtbh_nFFsTg-q2mNU/edit?usp=sharing

### Overview
In this variant of Blackjack, the player starts with $500 and plays against the dealer. In each round, the player can deal or stand until the value of their hand reaches or exceeds 21. The dealer must deal with a hand below 17, and must stand with a hand above or equal to 17. Blackjacks give 1.5x return to the player.

### Setup
1.  Clone the brandonhudavid/blackjack repo
2. Navigate to the cloned directory and run `python Blackjack.py`

### Implementation 
`Blackjack.py` contains the main logic for the game. Specific tasks are delegated to classes in `Card.py`, `Deck.py`, `Person.py`, and `Player.py`.

### Technologies
`random` - chooses a random Card within Deck

`time` - to suspend code execution and improve user experience

`sys` - to exit the game when Player has no more money
