import random
import time

class Card:
	value = -1
	def __init__(self):
		rand = random.randint(1, 66)
		#time.sleep(1)
		if(1 <= rand <= 4):
			self.value = 0
		if(5 <= rand <= 8):
			self.value = 1
		if(9 <= rand <= 12):
			self.value = 2
		if(13 <= rand <= 16):
			self.value = 3
		if(17 <= rand <= 20):
			self.value = 4
		if(21 <= rand <= 24):
			self.value = 5
		if(25 <= rand <= 28):
			self.value = 6
		if(29 <= rand <= 32):
			self.value = 7
		if(33 <= rand <= 36):
			self.value = 8
		if(37 <= rand <= 45):
			self.value = 9
		if(46 <= rand <= 54):
			self.value = 10 #Tausch
		if(55 <= rand <= 61):
			self.value = 11 #Druntergucken
		if(62 <= rand <= 66):
			self.value = 12 #Nochmal ziehen

	def getValue(self):
		return self.value
	
	def __str__(self):
		if(0 <= self.value <= 9):
			return "  " + str(self.value) + "  "
		elif(self.value == 10):
			return "Swap "
		elif(self.value == 11):
			return "Look "
		elif(self.value == 12):
			return "Again"

class Player:
	cards = 0
	handcard = 0
	name = ""
	def __init__(self):
		self.cards = []
		for i in range(4):
			self.cards.append(Card())

	def getCardValue(self, cardnr):
		if(0 <= cardnr < 4):
			return self.cards[cardnr].getValue()

	def getCardStr(self, cardnr):
		if(0 <= cardnr < 4):
			return str(self.cards[cardnr])

	def getCard(self, cardnr):
		if(0 <= cardnr < 4):
			return self.cards[cardnr]

	def setCard(self, cardnr, card):
		if(0 <= cardnr < 4):
			self.cards[cardnr] = card

	def getTotalCardValue(self):
		count = 0
		for i in range(4):
			if(self.cards[i].getValue() <= 10):
				count += self.cards[i].getValue()
			else:
				count += 10

	def setHandCard(self, card):
		self.handcard = card

	def getHandCard(self):
		return self.handcard

	def getHandCardValue(self):
		return self.handcard.getValue()

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setCardAsHandcard(self, cardnr):
		self.cards[cardnr] = handcard
		handcard = 0

	def getFullInfo(self):
		info = self.name + ": "
		for i in range(4):
			info += str(self.cards[i])
		info += str(self)
		return info

class Game:
	players = []
	currentPlayer = 0
	stapleOpenCard = Card()
	stopped = False
	def __init__(self, playercount):
		if (1 <= playercount <= 6):
			for i in range(playercount):
				self.players.append(Player())
		else:
			print("Player Number must be between 1 and 6")

	def drawStapleRandom(self, player):
		player.setHandCard(Card())

	def drawOpenStaple(self, player):
		player.setHandCard(stapleOpenCard)
	
	def playerExchangesCard(self, player, cardnr):
		if(1 <= cardnr <= 4):
			player.setCard(cardnr - 1)
		else:
			print("Cardnumber must be between 1 and 4.")

	def playerLooksAtCard(self, player, cardnr):
		if(player.getHandCardValue() == 11):
			return player.getCardValue(cardnr)

	def playerExchangesOtherPlayersCard(self, player, otherPlayer, cardnr, othercardnr):
		if(player.getHandCardValue() == 10):
			card = player.getCard(cardnr)
			player.setCard(cardnr, otherPlayer.getCard(othercardnr))
			otherPlayer.setCard(othercardnr, card)

	def playerPutsCardOnStaple(self, player):
		self.stapleOpenCard = player.getHandCard

	def playerStops(self, player):
		self.stopped = True

	def consoleGUIstart(self):
		inp = 0
		for i in range(len(self.players)):
			print("Player " + str(i + 1) + ", give me a name!")
			self.players[i].setName(input())
			print("Your Cards: (5 Seconds of display)")
			print ("[" + self.players[i].getCardStr(0) + "] + [  X  ] + [  X  ] + [" + self.players[i].getCardStr(3) + "]", end="\r")
			time.sleep(2)
			print("                                      ")
		while (self.stopped == False):
			print("Player " + self.players[self.currentPlayer].getName() + ", its your turn.")
			while(True):
				print("Do you want to")
				print(" [1] Draw a random card from the staple or")
				print(" [2] Draw the [" + str(self.stapleOpenCard) + "] card from the open Staple")
				inp = int(input())
				if(1 <= inp <= 2):
					break
				print("Wrong Input")
			if(inp == 1):
				self.drawStapleRandom(self.players[self.currentPlayer])
			if(inp == 2):
				self.drawOpenStaple(self.players[self.currentPlayer])
			if(self.players[self.currentPlayer].getHandCardValue() == 10):
				pass#TODO: Tausch
			elif(self.players[self.currentPlayer].getHandCardValue() == 11):
				pass#TODO: Drunter Gucken
			elif(self.players[self.currentPlayer].getHandCardValue() == 12):
				pass#TODO: Nochmal Ziehen
			else:
				pass#TODO: Normale Zahlenkarte
			print("Your Handcard is: [" + str(self.players[self.currentPlayer].getHandcard()) + "]")
			if(self.currentPlayer < (len(self.players) - 1)):
				self.currentPlayer += 1
			else:
				self.currentPlayer = 0
			print(self.players[self.currentPlayer].getFullInfo())
			time.sleep(1)



print("How many Players: ")
pn = int(input())
g = Game(pn)
g.consoleGUIstart()

