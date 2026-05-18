'''
Your program will create a DeckOfCards object using your DeckOfCards class.  This object will contain a list of 52 Card objects. The DeckOfCards Class already contains a shuffle_deck() function to shuffle a new deck, and a get_card() function returns the next card in the deck (card at index 0 in the list).  

Your program must print the deck of cards before, and after, they are shuffled (I want to see they are being shuffled properly). 

Your program must also be able to correctly score the card based on the suit.  i.e...

 

“2 of Spades” = 2 points

“3 of Spades" = 3 points

…

 

“9 of Spades" = 9 points

“10 of Spades" = 10 points

“Jack of Spades" = 10 points

“Queen of Spades" = 10 points

“King of Spades" = 10 points

“Ace of Spades" = 11 points or 1 point (Details on how to implement this below (it's actually not hard))
'''

#  building out my deck of cards

# importing libraries I will use in my code 
import random 

# Card() is a supporting class to the DeckOfCards() class below 
class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

# establishig the class that builds the actual deck of cards
class DeckOfCards():
    def __init__(self, deck=[]):
        self.deck = deck

    # function to shuffle the deck - using the random library to shuffle the cards in the deck list
    def shuffleDeck(self):
        random.shuffle(self.deck)

    # function to print deck 
    def printDeck(self):
        for card in self.deck:
            print(card.face, 'of', card.suit)

    # function to get a card 
    def getCard(self):
        return self.deck.pop(0) # removes the first item from the shuffled deck
    
    # function to put cards back into the deck (used to restore the full 52 between rounds and prevent pop from empty list error)
    def addCards(self, cards):
        self.deck.extend(cards)

# establishing two lists showing the possible suit or face the card could be
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# nested for loops to actually go through and build the deck 
cards = []
for suit in suits:
    for face in faces:
        # using our Card() class to build each card
        cards.append(Card(suit, face))

# using our DeckOfCards() class to pass in our cards we just built and create the deck of cards
deck = DeckOfCards(cards)

# testing to confirm the deck was built correctly 
deck.printDeck()
print('--------------------')
# shuffle deck
deck.shuffleDeck()
deck.printDeck()

