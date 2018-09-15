# poker-hand-comparator
These scripts serve to compare two Texas Hold'Em hands, on a given board, to determine which one wins.

## Contact
@author Tyler Fisher (tjfisher[at]gmail[dot]com)
@date Feb 2017. Modified Sep 2018.

## Requirements
Python 2.7+ (tested with version 2.7.9). Not specifically compatible with Python 3.0+.

## Usage
In Terminal, cd into this repo, then run the following:
`python generateAndCompare.py`

This will randomly generate a five-card board, plus two sample hands of two cards each. It'll then tell you which one won, and what each hand's value is.

The other scripts in this repo enable you to enter specific hands through the terminal. The scripts in the heads-up folder are for a two-player game; the scripts in the multiplayer folder are for games with three or more players.

## The code
Each of these scripts runs on simple text inputs and outputs. The outputs should all be straightforward enough to decipher. If you're unclear on my use of symbols, they're the standard poker hand notation. I give an overview of what that means at the bottom of this README.

NOTE: There is *no* error-checking implemented, because the idea of the code was to make it as short as possible, and we were assuming that we would feed correct inputs into the programs. So, if you feed too many cards, or non-card characters, or anything else that's wrong, it'll probably just break or do something weird. It'll work if you enter your input correctly, as commented in the scripts.

NOTE: If a script has a weird name and the code looks strange and ugly, it's because I was playing code golf with it. That is, I was trying to make it as short as possible, for a contest with a friend. (Indeed, that friend's code can be found in the file `ekshesh-code.py`.) The shortened not really meant to be legible, just functional in as few lines (or characters) as possible. If you're trying to see how it works, I recommend you look at `generateAndCompare.py`. If you're digging in any other file, beware my random variable names. (Though, some are actually commented fairly well. I wrote this 18 months ago, in just a few hours while procrastinating from studying for a midterm, so forgive me.)


<hr>
# Poker for dummies
I'll give a brief rundown of what it actually MEANS to compare two hands in poker, in case you're unsure what this is all about. The below information is enough to compare any two or more hands in Texas Hold'Em against one another. Indeed, it's enough for any seven-card poker game. I'm not going to explain how the game actually works, just how to compare two hands once you've already gotten to the end of the hand, all the cards are on the table, and all the betting is over.

## Basic rules of texas hold'em
You have 2 cards, as do each of your opponents. There will be dealt 5 cards in the middle. Those are for everyone to share. Out of your 7 total cards, you want to make the best possible hand *of 5 cards*. You only care about the 5 cards that comprise the best hand. The other 2 left over are irrelevant. It does NOT matter whether the cards are 2 from your hand + 3 from the board, or 1 + 4, or 0 + 5. The best 5-card hand wins. If two or more hands are of the same value, it's a draw.

## Basic card info
Here are examples of individual cards: 2h (2 of hearts); Td (ten of diamonds); As (ace of spades).
The first character is the card's rank, and the second character is its suit.
### RANK (card number)
* 2, 3, 4, 5, 6, 7, 8, and 9 correspond to those exact numbered cards.
* T, J, Q, K, and A refer to ten, jack, queen, king, and ace, respectively.
* T (ten) is worth 10, as you'd expect. J (jack) is 11; Q (queen) is 12; and K (king) is 13.
* A (ace) is 14, and is thus the highest card. An ace can also act as a 1 if needed.
* * note: an ace can act as EITHER a 1 or a 14, but not both simultaneously.
* higher cards are better than lower cards
### SUIT (symbol)
* s = spades; h = hearts; c = clubs; d = diamonds
* all suits are equivalently valuable

## Terminology and hand-related information:
* the term "pair" means 2 cards of the same rank (number)
* "three-of-a-kind" and "four-of-a-kind" mean 3 or 4 cards of the same rank
* ("five-of-a-kind" can't exist, because there are only 4 cards of each rank in a deck)
* "two pair" means two *different* pairs (for example, two 8s and two Ks)
* ("three pair" can't exist because hands only consist of 5 cards, and three pairs would require 6)

* "straight" means five consecutive cards, by rank (for example, 2-3-4-5-6 or 9-T-J-Q-K)
* * this means that A-2-3-4-5 and T-J-Q-K-A are both straights
* * however, something like Q-K-A-2-3 is NOT a straight (it doesn't "wrap around")
* "flush" means five cards of the same suit. It doesn't matter what ranks they are

## Hand rankings, in order from best to worst:
* Straight flush: 5 consecutive cards, all of the same suit. (approximate rarity: 1/3200 hands)
* Quads: four-of-a-kind. 4 cards of the same rank. (approximate rarity: 1/590 hands)
* Full house: three-of-a-kind of one card, AND a pair of another. (approximate rarity: 1/38 hands)
* Flush: five cards of the same suit. WHICH suit does not matter. (approximate rarity: 1/32 hands)
* Straight: five consecutively ranked cards. Suits don't matter. (approximate rarity: 1/21 hands)
* Trips: three-of-a-kind. 3 cards of the same rank. (approximate rarity: 1/20 hands)
* Two pair: two different pairs of cards of the same ranks. (approximate rarity: 1/3.3 hands)
* One pair: one pair of cards of the same rank. (approximate rarity: 1/1.3 hands)
* [X]-high: none of the above. The "X" is whatever your highest ranking card is.

## Comparing two hands
* The player with a hand that is higher up on that hierarchy wins.
* - Usually this simply means determining which player has higher ranked cards.
* If two players are at the same step of the hierarchy, the tie-breaker goes as follows:
* - When comparing pairs, the one that is a higher rank wins. So, `two aces` beats `two 7s`. If the pairs are the same (i.e. both players have two 9s), then look at the next highest card each player has. (Remember a player's hand is made up of FIVE cards, and the pair is only the first two of those.) If that next highest card, called the "kicker", is still the same, then look at the next highest card after that, and then the next highest card after that. The hand can only be a draw if the pair is the same, AND all three kickers are all the same. So, if two players have the same pair, but one also has a Q, T, and 5, that player beats someone else who has a Q, 8, and 7, or someone who has a J, T, and 9, or even someone who has a Q, T, and 4.
* - When comparing two-pairs, first compare the higher pair, and, if it's still tied, then compare the lower one. So, `two kings and two 9s` beats `two kings and two 6s`, and they both beat `two jacks and two tens`. If BOTH pairs are the same, look at the next highest card (i.e. the fifth card) and see which one is higher. So, two pairs with a king as the "kicker" beats the same two pairs with a 7 as the "kicker".
* When comparing trips (three-of-a-kind), check the first and second "kickers", same as when comparing pairs. As soon as one player has a better kicker, that player wins.
* When comparing quads (four-of-a-kind), check the one kicker that remains, same as above.
* When comparing full-houses, first compare the three-of-a-kind. If it's the same for both players, then compare the pair. If that's the same, too, that is already 5 cards, so there are no kickers to check & the players draw.
* - When comparing straights, the one that *ends* higher wins. So, `3-4-5-6-7` beats `A-2-3-4-5`. There are no kickers, because a straight must consist of 5 cards already.
* - When comparing flushes, the one with the highest card within that flush wins. If they have the same highest card, then the second-highest suited card wins. If it's still tied, then check the third, fourth, and fifth. So, a flush of `A-K-9-8-5` beats a flush of `A-K-9-7-6`. There are no kickers, because a flush consists of 5 cards already.

## Other terminology you may see in the code, especially in the comments
* "SF" means straight flush
* "boat" is equivalent to "full house", i.e. three-of-a-kind plus a separate pair.
* "set" is equivalent, for the sake of this code anyway, to "trips", i.e. three-of-a-kind
* "chop" means draw, or tie (as in you "chop" the pot into equal pieces and give it equally to each of the tie-ing players)


# Minutiae / FAQ
Q: "But a *royal* flush is the best hand in the game! Why did you say a straight flush is the best possible hand??"
A: A royal flush *is* just a straight flush, that happens to consist of the cards T-J-Q-K-A. There's nothing special about it beyond that. It isn't its own "type" of hand. It's just like how a grand slam is still just a home run, albeit a really great and fairly rare one.
*
Q: Aren't spades the best suit? Isn't the ace of spades the best card?
A: No. They're all the same in poker.
*
Q: If the best 5 cards always win, how does poker involve any skill? Sounds like all luck of the deal.
A: The best hand only wins if it gets to the end of the hand. If the person holding it folds before that, because she doesn't want to bet, she's forfeited the hand and allowed a worse hand to win. In any single hand there's a fair luck factor, but over the course of several or many hands, it's almost all skill, to the point that a beginner will lose to a professional 9999 times out of 10000.

Also, that question has nothing to do with this code.
*
