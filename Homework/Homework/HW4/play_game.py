'''
Program Requirments:

1.  Rules of the game:

The user will always win if…

-User score does not exceed 21, and is higher than the dealer’s score.

-User score does not exceed 21, and the dealer “busts” (gets a score higher than 21).

The user will always lose if…

-User “busts” (gets a score higher than 21)

-User score does not exceed 21, but the dealer’s score is equal or higher and also does not exceed 21.

 

 

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

 

2.  Playing the game

To begin the game, your program should have a welcome message, create the deck of cards, shuffle the deck, deal two cards to the user, two cards to the dealer (don't display the dealer's cards yet, just keep track of them).  Print the current user's score to the screen, and ask the user if they would like a ‘hit’.  Continue asking the user if they would like a hit until they stop, or their score exceeds 21.  If the user’s score exceeds 21 print a losing message to the screen. 

If the user has not exceeded 21, and stopped hitting, then display the two dealer's cards.  Have the Dealer keep hitting while the dealer's score is under 17.  Then calculate the dealer’s score, determine if the user won or lost, print the results, and ask the user if they would like to play again.

If the user chooses to play again, keep using the same deck.  Do not create a new deck.  You can simply shuffle the deck again.  You do not need to exclude the cards that have been dealt to the user.  You can simply shuffle the whole deck of 52 cards again.  You can see how this works in the sample output below.  Print the deck before and after it is shuffled, so I can verify your shuffle_deck() and deal_card() functions are working properly.

 

3.  Handling an Ace

An Ace has the value of 1 or 11 in BlackJack.  The user is in charge of when they hit, and they can keep track themselves what the value of an Ace should be.  Meaning your program simply has to keep track of how many aces the user, or the dealer, has.  If an Ace is present in the hand, and the score busts then reduce the score by ten automatically, so it is no longer busted.  Your program should also be able to do this multiple times to account for a hand with multiple Aces.

 

Other Requirements

 

- Have a separate file for DeckOfCards.py and play_game.py

- Card class definition can be in DeckOfCards.py 

- play_game.py should import DeckofCards

from DeckOfCards import *

 

- All the logic for playing the game should be in play_game.py

Note: In the DeckOfCards.py, there is logic in that file, but logic for playing the game should no go in there. 

- For each of the possible ways to win or lose, mentioned above, print a message to the user stating why they won or lost.  i.e. if the dealer busted print “Dealer busted, you win!” (or similar).

 

- As mentioned, when you shuffle the deck, print the deck before and after the shuffle.  

 

If you are unfamiliar with the game of BlackJack (or 21) you can familiarize yourself here: https://en.wikipedia.org/wiki/BlackjackLinks to an external site.  (You are not required to read this)
'''


# importing libraries or classes used
from DeckOfCards import *

# welcome message with new line spaces for easy readability 
print('Welcome to Black Jack! \n \n')

# building the deck of cards 
# nested for loops to actually go through and build the deck 
cards = []
for suit in suits:  
    for face in faces:
        # using our Card() class to build each card
        cards.append(Card(suit, face))

# using our DeckOfCards() class to pass in our cards we just built and create the deck of cards
deck = DeckOfCards(cards)

# establishing user hand & dealer hand outside of play again loop
user_hand = []
dealer_hand = []

# putting the entire program in a loop so the user can easily play again 
play_again = 'y'

while play_again =='y':
    # return last round's cards to the deck before reshuffling 
    # (on round 1 these are empty so nothing happens)
    deck.addCards(user_hand)
    deck.addCards(dealer_hand)
    user_hand = []
    dealer_hand = []

    # printing cards before they were shuffled and after they are shuffled
    print('DECK BEFORE BEING SHUFFLED')
    deck.printDeck()
    print('-------------------- \n \n')
    # shuffle deck
    print('DECK AFTER BEING SHUFFLED')
    deck.shuffleDeck()
    deck.printDeck()
    print('-------------------- \n \n')

    # logic to handle the conversion from deck of cards 
    # dictionary mapping each face to its blackjack point value
    # Ace defaults to 11; the "1 or 11" decision happens when scoring the whole hand
    card_values = { 
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10,
    'Ace': 11,
}

    # function to total a hand that converts aces from 11 to 1 if the hand would bust
    def handTotal(cards):   
        total = 0
        aces = 0
        for card in cards:
            total += card_values[card.face]
            if card.face == 'Ace':
                aces += 1
    
    # if the hand busts and there is at leaste one ace, change the value of the ace from 11 to 1 by subtracting 10
    # putting inside a loop in case there are multiple aces 
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    # function to return the point value of a single card based on its face
    def cardValue(card):    
        return card_values[card.face]

    # giving two cards to the dealer and the user by calling the getCard() function I added to the DeckOfCards class! 
    user_hand.append(deck.getCard())
    user_hand.append(deck.getCard())
    dealer_hand.append(deck.getCard())
    dealer_hand.append(deck.getCard())

    # showing the user their current score 
    print('Your Cards:')
    card_number = 1
    for card in user_hand:
        print('Card', card_number, 'is', card.face, 'of', card.suit)
        card_number += 1
    print('Your score:', handTotal(user_hand)) # passing in the user hand to the previously established handTotal() function 

    # asks the user if they would like another hit after they recieve their score(converts their answer to lower case and trimming white space)
    hit = input('Would you like a hit? y/n ').lower().strip()

    # if yes, retrieve another card for the user 
    while hit == 'y':
        card_number += 1
        new_card = deck.getCard()
        user_hand.append(new_card)
        print('Card', card_number, 'is', new_card.face, 'of', new_card.suit)
        print('Your score:', handTotal(user_hand))

        # if the user score is over 21, they are a loser so stop the game 
        if handTotal(user_hand) > 21:
            break

        # see if the user wants another card if they're under 21
        hit = input('Would you like a hit? y/n ').lower().strip()

    # logic to tell the user they lost if their hand total > 21 
    user_busted = False
    if handTotal(user_hand) > 21:
        print('You busted! You lose.')
        user_busted = True

    # put final user score in a variable
    final_user_score = handTotal(user_hand)

    # logic to manage dealer hand draw up to 17
    while handTotal(dealer_hand) < 17:
        dealer_hand.append(deck.getCard())
   
    # show the dealer hand and score if the user didn't bust 
    if user_busted == False:
        dealer_card_number = 1

        for card in dealer_hand:
            print('Card', dealer_card_number, 'is', card.face, 'of', card.suit)
            dealer_card_number += 1

        final_dealer_score = handTotal(dealer_hand)
        print('Final dealer score is:', final_dealer_score)

        # logic to handle the dealer busting 
        dealer_busted = False
        if final_dealer_score > 21:
            print('The dealer busted, you win!')
            dealer_busted = True

        # compare final scores to see who won 
        final_message_printed = False
        while final_message_printed == False:
            if final_dealer_score > final_user_score and dealer_busted == False:
                print('The dealer scored higher, you lose!')
            if final_dealer_score == final_user_score and dealer_busted == False:
                print('Your scores are the same, you lose!')
            if final_dealer_score < final_user_score and dealer_busted == False:
                print('Congratulations, you win!!')
            # changing final message printed to true to force exit the while loop
            final_message_printed = True

    # asks the user if they want to play again 
    play_again = input('Would you like to play again? y/n ').lower().strip()






