# Written by Tyler Fisher, 21 Feb 2017

import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["s", "h", "c", "d"]

randomHand = ranks[random.randrange(0, 13)] + suits[random.randrange(0, 4)]
for i in range(8):
	randomCard = randomHand
	while randomCard in randomHand:
		randomCard = ranks[random.randrange(0,13)]+suits[random.randrange(0,4)]
	randomHand += randomCard
	if i==0 or i==2: randomHand += " "

print randomHand
