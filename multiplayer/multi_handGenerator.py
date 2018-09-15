# Written by Tyler Fisher, 21 Feb 2017
import random
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["s", "h", "c", "d"]

def getRandomCard(handSoFar):
	randomCard = ranks[random.randrange(0, 13)] + suits[random.randrange(0, 4)]
	while randomCard in handSoFar:
		randomCard = ranks[random.randrange(0, 13)] + suits[random.randrange(0, 4)]
	return randomCard

randomHand = ''
for fiveTimes in range(5): randomHand += getRandomCard(randomHand) # board
numAdditionalHands = random.randrange(1, 10) # how many more players (1-9 more)

for whatever in range(numAdditionalHands):
	randomHand += " "
	randomHand += getRandomCard(randomHand) # first pocket card
	randomHand += getRandomCard(randomHand) # second pocket card

print randomHand
