class Player(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []
        self.currentBet = 0
        self.winStatus = False
        self.bust = False

    def hand(self):
        print("{} has ".format(self.name), end="")
        for i in range(len(self.cards)):
            if i > 0:
                print(", ", end="")
            if i == (len(self.cards) - 1) and len(self.cards) >= 1:
                print("and ", end="")
            self.cards[i].showCard()
        return self.totalScore()

    def addCard(self, Card):
        self.cards.append(Card)

    def askToBet(self):
        while True:
            print("How much do you want to bet?")
            wage = int(input())
            if wage > self.money:
                print("You don't have enough funds.")
                continue
            else:
                print("Luis bet ${}".format(wage))
                self.money -= wage
                self.currentBet = wage
                print("He has ${} left".format(self.money))
                break;

    def totalScore(self):
        total = 0
        for i in range(len(self.cards)):
            total += self.cards[i].getPlayableValue()  # doesn't incorporate Ace yet
        return total

    def hasMoney(self):
        if self.money <= 0:
            print("You lost all your money. Go home and begin filing your divorce papers.")
            return False
        return True

    def getMoney(self):
        return self.money

    def wagerWon(self, wage):
        self.money += wage

    def getName(self):
        return self.name

    def getCards(self):
        return self.cards

    def clearHand(self):
        self.cards = []
        self.currentBet = 0
        self.bust = False

    def roundBet(self):
        return self.currentBet

    def playerWon(self):
        self.winStatus = True

    def hasPlayerWon(self):
        return self.winStatus

    def playerBust(self):
        return self.bust

    def bustPlay(self):
        self.bust = True
