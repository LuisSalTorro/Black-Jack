# an array with suit and value
class Card(object):
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def showCard(self):
        value = self.value
        if value == 1:
            value = "Ace"
        elif value == 11:
            value = "Jack"
        elif value == 12:
            value = "Queen"
        elif value == 13:
            value = "King"
        print("{} of {}".format(value, self.suite), end="")

    def getTrueValue(self):
        return self.value

    def getPlayableValue(self):
        # for jack, queen, and king, return 10
        if self.value == 11: #jack
            return 10
        if self.value == 12: #queen
            return 10
        if self.value == 13: #king
            return 10
        return self.value

    def getSuite(self):
        return self.suite
