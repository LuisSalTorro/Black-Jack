from Deck import Deck


class Dealer(object):
    def __init__(self):
        self.Deck = Deck()
        self.__shuffle()
        self.cards = []
        self.winStatus = True
        self.bust = False
        self.matchBet = 0

    def makeBet(self,playerBet):
        self.matchBet += playerBet

    def getMatchBet(self):
        return self.matchBet

    def clearHand(self):
        self.cards = []
        self.bust = False
        self.matchBet = 0

    def __shuffle(self): #creates new deck
        self.Deck = Deck()
        self.Deck.shuffle()

    def deal(self):
        return self.Deck.topCard()

    def checkCardsLeftInDeck(self):
        if len(self.Deck) < 20:
            self.__shuffle()

    #skip card[0] to keep it unknown until the end.
    #also, stop picking up cards when dealer has a total of 17 points
    def hand(self):
        print("Dealer has ", end="")
        for i in range(len(self.cards)):
            if i > 0:
                print(", ", end="")
            if i == (len(self.cards) - 1) and len(self.cards) >= 1:
                print("and ", end="")
            self.cards[i].showCard()
        return self.totalScore()

    def addCard(self, Card):
        self.cards.append(Card)

    def totalScore(self):
        total = 0
        for i in range(len(self.cards)):
            total += self.cards[i].getPlayableValue()  # doesn't incorporate Ace yet
        return total

    def getCards(self):
        return self.cards

    def playerWon(self):
        self.winStatus = True

    def hasPlayerWon(self):
        return self.winStatus

    def playerBust(self):
        return self.bust

    def bustPlay(self):
        self.bust = True