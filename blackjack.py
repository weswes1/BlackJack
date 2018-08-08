import random


suit=[2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING","ACE"]
gdeck=suit*4
random.shuffle(gdeck)

class player:
	def __init__(self,funds=0,hand=[]):
		self.funds = funds
		self.hand = hand

class dealer:
	def __init__(self,deck=[],hand=[]):
		self.deck=deck
		self.hand=hand

	def distributeCard(self):
		distributed = self.deck.pop()
		return distributed
		#return deck[]

def initializePlayer():
	newplayer=player()
	funds=-1
	while (type(funds)!=float or newplayer.funds<0):
		funds = float(input("Enter the number of funds you would like to add to play with: "))

	newplayer.funds = funds
	return newplayer



def play():
		anewdealer=dealer(random.shuffle(gdeck))
		if (askplay()==True):
			anewplayer = initializePlayer()
			print ("a new player has {} ".format(anewplayer.funds))
			bet = askbet(anewplayer)

				anewplayer.hand.append(newdealer.distributeCard())
				anewplayer.hand.append(newdealer.distributeCard())
				anewdealer.hand.append(newdealer.distributeCard())
				anewdealer.hand.append(newdealer.distributeCard())

				ins=""
				while (ins != "hit" or ins != "stand"):
					ins = input("Hit or stand?")
					if (ins == "stand"):
						pass
		# The player doesn't want to play
		else:
			print("hit")
			pass



def askplay():
	ans = ""
	while (ans!="Y" or ans!="N"):
		ans=input("Would you like to play Blackjack, enter Y / N").capitalize()
		if (ans=="Y"):
			break
		if (ans=="N"):
			break
	return ans=="Y";



def askbet(player):
	bet = -1
	while (type(bet)!=float or bet < 0 or player.funds < bet):
		bet=input("Enter how much you would like to bet, it must be available.")
		float(bet)

	return bet;


play()

def over21(num):
	return num>=21