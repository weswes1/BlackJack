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
	anewdealer=dealer(random.shuffle(gdeck),"")
	if (askplay()==True):
		anewplayer = initializePlayer()
		print ("a new player has ${} in funds".format(anewplayer.funds))
		bet = askbet(anewplayer)

		dealer_sum=0
		player_sum=0

		for i in range(0,2):
			dealersum+=
			anewplayer.hand.append()
			anewdealer.hand.append(anewdealer.distributeCard())
	

		while (not over21(dealer_sum) and not over21(player_sum)):
			pass




	# The player doesn't want to play
	else:
		print("Not playing")
		pass



def askplay():
	ans = ""
	while (ans!="Y" or ans!="N"):
		ans=input("Would you like to play Blackjack, enter Y / N ").capitalize()
		if (ans=="Y"):
			break
		if (ans=="N"):
			break
	return ans=="Y";




def hitstand():
	ins=""
	while (ins != "hit" or ins != "stand"):
			ins = input("Hit or stand?").lower()
			if (ins == "stand"):
				return "stand"
			elif (ins=="hit"):
				return "hit"

def askbet(player):
	bet = -1
	while (type(bet)!=float or bet < 0 or player.funds < bet):

		bet=input("Enter how much you would like to bet, it must be available. ")
		bet = float(bet) # What if bet is not a number ? 

		if (player.funds < bet):
			print ("You don't have enough money to make that bet. ")

		elif (bet<0):
			print("The number can't be less than zero! ")

	return bet;


# play()

def over21(num):
	return num > 21









"""
aplayer = player()
frank = dealer(gdeck);
#nprint(frank.deck)
print("number of cards in dealer's deck: \n")
print(len(frank.deck))
print("number of cards in dealer's hand: \n")
print(len(frank.hand))
print("number of cards in player's hand: \n")
print(len(aplayer.hand))

card_1 = frank.distributeCard()
card_2 = frank.distributeCard()

frank.hand.append(card_1)
aplayer.hand.append(card_2)

sum = card_1+card_2

print("the dealer distributed a card to himself and a player... ")
print("number of cards in deck: \n")
print(len(frank.deck))
print("number of cards in dealer's hand: \n")
print(len(frank.hand))
print("number of cards in player's hand: \n")
print(len(frank.hand))
"""
