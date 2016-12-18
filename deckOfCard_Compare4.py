# Required dependencies
from random import shuffle

# Deck of cards

class Card(object):
    def __init__(self, suit, value, image=None):
        self.suit = suit
        self.value = value
        self.image = image

class Deck(object):
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.deck = []
        self.buildDeck()

    def buildDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))
        self.shuffle()
        return self

    def shuffle(self):
        shuffle(self.deck)
        return self

    def deal(self):
        if self.deck: # empty lists return as False
            # removes and returns card from deck, shuffled or not
            return self.deck.pop()
        else:
            print "No more cards"

    def returnCard(self, card, reShuffle = False):
        self.deck.append(card)
        if reShuffle:
            self.shuffle()
        print self.deck

    def resetDeck(self):
        self.deck = []
        self.buildDeck()
        # print self


# # GAME LOGIC
                

# def show


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]  ### Sets the suits
values = range(1,14)  ### Sets the range for each suit
deck = Deck(suits, values)  ### Each deck has cards with a value and suit

### Created a poor sap who can only gamble and do what we tell them to do

class Player(object):
    def __init__(self, image=None):
        self.image = image
        self.hold = []

    ### Everytime player draws a card
    ### a card is removed from the deck and placed in Player's hand
    def drawcard(self):
        self.card = deck.deck.pop()
        self.hold.append(self.card)

### >>>!!!COMPARE 4 LUCK!!!<<<
### Easy and fast game for kids!
### Two players draw four cards
### Then compare the cards to see who wins
### May be based entirely on luck...or rigging ~_^
class Compare4Luck(object):

    def __init__(self):

        self.Player1Score = 0
        self.Player2Score = 0

    def drawCards(self):
        
        CardNumber = 4 ### How many cards we want each player to draw

        for z in range(0,CardNumber):  ## We deal each player the amount of cards
            Player1.drawcard()
            Player2.drawcard()

        ### We print out the value and suit of each card in each player's hold
        for x in xrange(0,len(Player1.hold)):
            print "Player 1:", Player1.hold[x].value, "of", Player1.hold[x].suit

        for x in xrange(0,len(Player2.hold)):
            print "Player 2:", Player2.hold[x].value, "of", Player2.hold[x].suit

        ### Compares the cards and adds scores for each player
        Player1Score = 0
        Player2Score = 0
        for x in range(0,CardNumber):
            if Player1.hold[x].value > Player2.hold[x].value:
                Player1Score +=1
            # if Player2.hold[x].value > Player1.hold[x].value:
            if Player2.hold[x].value > Player1.hold[x].value:
                Player2Score +=1
            else:
                Player1Score +=1
                Player2Score +=1

        ### Prints total scores for each player
        print "\nTotal score for Player 1:", Player1Score
        print "Total score for Player 2:", Player2Score

        ### Conditions on which player will win or if they tie.
        if Player1Score > Player2Score:
            print "\n YAY!! Player 1 wins!!!!! \n"
        if Player1Score < Player2Score:
            print "\n WTF Player 2 wins?!?!? \n"
        if Player2Score == Player1Score:
            print "\n You tied... T_T \n"
        # else:
        #     print "\n You tied... T_T \n"


Player1 = Player() ### Player 1 is initialized
Player2 = Player() ### Player 2 is initialized
Game1 = Compare4Luck()  ### Initialize the game

Game1.drawCards()  ### Play the game