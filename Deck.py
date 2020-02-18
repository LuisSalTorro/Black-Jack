from Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.__createCards()

    def __createCards(self):
        self.cards = []
        suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
        for i in range(len(suites)):
            for j in range(1, 14):
                self.cards.append(Card(suites[i], j))

    def topCard(self):
        return self.cards.pop()

    def shuffle(self):
        tempCards = self.cards
        boilCards = [0] * len(tempCards)
        for i in range(len(self.cards)):
            number = random.randrange(0, len(tempCards))
            boilCards[i] = tempCards.pop(number)
        self.cards = boilCards
