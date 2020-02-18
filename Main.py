import time

from Player import Player
from Dealer import Dealer
from Board import Board


def firstPlay():
    answer = input("Will you bet? {} has ${}.\n".format(player.getName(),player.getMoney()))
    if "Yes" in answer or "yes" in answer or "y" in answer:
        player.askToBet()
        playBet = player.roundBet()
        dealer.makeBet(playBet)
        board.betTable(playBet+dealer.getMatchBet())
        player.addCard(dealer.deal())  # deals first card
        player.addCard(dealer.deal())
        dealer.addCard(dealer.deal())
        dealerPoints = dealer.hand()
        board.checkCards(dealerPoints, dealer.getCards(), dealer)
        return True
    elif "No" or "no" or "n" in answer:
        board.endGame()
        return False


def dealerPlay():
    print("{} has a total of {} points.".format(player.getName(), player.totalScore()))
    # This is where dealer begins to draw cards.
    # if dealer has 16 or less, he had to hit 17 or higher he has to stop
    while dealer.totalScore() < 17:
        time.sleep(1.5)
        dealer.addCard(dealer.deal())
        dealerPoints = dealer.hand()
        board.checkCards(dealerPoints, dealer.getCards(), dealer)
    # compare total score of dealer and player
    time.sleep(1.5)
    if not player.playerBust() and dealer.playerBust():
        print("{} won ${}!".format(player.getName(), board.getTableBet()))
        player.wagerWon(board.getTableBet())
    elif (not player.playerBust() and not dealer.playerBust()) and player.totalScore() == dealer.totalScore():
        print("Push. No winner.\n You got your ${} back.".format(player.roundBet()))
        player.wagerWon(player.roundBet())
    elif (not player.playerBust() and not dealer.playerBust()) and player.totalScore() > dealer.totalScore():
        print("{} won ${}!".format(player.getName(), board.getTableBet()))
        player.wagerWon(board.getTableBet())
    else:
        print("Dealer won.\n You lost ${}".format(player.roundBet()))
    # winners takes home money


def playGame():
    playerPoints = player.hand()
    board.checkCards(playerPoints, player.getCards(), player)
    if player.playerBust():
        print("You lost ${}".format(player.roundBet()))
        return False
    if player.totalScore() == 21:
        print("{} won ${}!".format(player.getName(), board.getTableBet()))
        return False
    answer = board.hitOrStay(player)
    if not player.playerBust() and "Hit" in answer or "hit" in answer:
        player.addCard(dealer.deal())
    else:
        dealerPlay()
        return False
    return True

player = Player("Luis", 500)
dealer = Dealer()
board = Board()
while player.hasMoney() and board.gameIsActive():
    board.newRound(player, dealer)
    print("New Round:\n")
    if firstPlay():
        while playGame() and board.roundIsActive():
            pass
