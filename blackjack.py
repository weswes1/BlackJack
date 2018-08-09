import random


suit=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
gdeck=suit*4
random.shuffle(gdeck)

class player:
	def __init__(self,funds=0,hand=[]):
		funds=-1
		while (type(funds)!=float or funds<0):
			funds = float(input("Enter the number of funds you would like to play with: "))
		self.funds = funds
		self.hand = hand

class dealer:
	def __init__(self,deck=[],hand=[]):
		self.deck=deck
		self.hand=hand

	def distributeCard(self):
		return self.deck.pop()
		
def play():
	while (True):
		if (askplay()==True):
			anewplayer = player()
			anewdealer=dealer(gdeck)

			print ("a new player has ${} in funds".format(anewplayer.funds))
			bet = askbet(anewplayer)

			dealer_sum=0
			player_sum=0


			card_1 = anewdealer.distributeCard()
			card_2 = anewdealer.distributeCard()
			card_3 = anewdealer.distributeCard()
			card_4 = anewdealer.distributeCard()

			anewplayer.hand.append(card_1)
			anewplayer.hand.append(card_2)
			anewdealer.hand.append(card_3)
			anewdealer.hand.append(card_4)


			ccard_1 = convert(card_1)
			ccard_2 = convert(card_2)
			ccard_3 = convert(card_3)
			ccard_4 = convert(card_4)

			player_sum = ccard_3+ccard_4
			print()

			dealer_sum=ccard_1+ccard_2

			print ("Your hand is: {}. The total of this hand is {}".format(anewplayer.hand,player_sum))
			print ("The dealer is showing a {} face up and another card face down.".format(anewdealer.hand[0]))


			while (player_sum <= 21):
				if (player_sum==21):
					anewplayer.funds+=bet
					print ("a new player has a BlackJack. ${} added to funds".format(bet))
					pass

					if(hitstand()=="hit"):
						print("You have requested a hit.")
						card_5 = anewdealer.distributeCard()
						pass


					elif(hitstand()=="stand"):
						pass
		# The player doesn't want to play
		else:
			print("Not playing")
			break


def convert(card):
	if (card=="K" or card=="Q" or card=="J"):
		return 10
	elif (card=="A"):
		choose = 0
		while (choose!= 1 or choose!=11):
			choose = input("Would you like to choose a value of 11 or 1 for your Ace? ")
			int(choose)
			if (choose==11):
				return 11
			elif (choose==1):
				return 1
	else:
		return card


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


play()

def over21(num):
	return num > 21

def under21(num):
	return num < 21
