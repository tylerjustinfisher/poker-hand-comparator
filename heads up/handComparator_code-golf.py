# Written by Tyler Fisher, 20 Feb 2017. For sample boards, see https://goo.gl/19jGRx

def firstHandIsBetter(h1, h2): # given two hands, with the 5 cards + rank + relevant kicker details, say which wins
    if h1[5] != h2[5]: return h1[5] > h2[5] # different ranks
    if h1[5]==8 or h1[5]==4: return h1[2] > h2[2] if h1[2] != h2[2] else h1[4] < h2[4] if h1[4] != h2[4] else None # SF or straight: check middle card, and if equal check for Ace low.
    if h1[5]==5 or h1[5]==0: # flush or high card: check all five cards
        for wooper in range(5):
            if h1[4 - wooper] != h2[4 - wooper]: return h1[4 - wooper] > h2[4 - wooper]
        return None # chop
    for scromp in range(6,10):
        if h1[scromp] != h2[scromp]: return h1[scromp] > h2[scromp] # one is higher, so that one wins
        if len(h1) == scromp+1: return None # all were the same, so it's a chop

def getBestFrom7(sevenCards, sevenSuits): # given 7 cards, call the 5-card comparator on each of the 21 poss. combos
    bestHand = None
    for i in range(7):
        for j in range(i+1, 7):
            s = []
            for k in range(7):
                if k != i and k != j: s.extend([sevenCards[k], sevenSuits[k]])
            newHand = getHandRankFromFiveCards(sorted([s[0],s[2],s[4],s[6],s[8]]), [s[1],s[3],s[5],s[7],s[9]])
            if bestHand is None or firstHandIsBetter(newHand, bestHand): bestHand = newHand
    return bestHand

def getHandRankFromFiveCards(fC, fS): # given 5 cards, determine what the rank of the hand is and add kicker info to it
    if fS.count(fS[0])==len(fS): fC.append(8) if ((fC[0]==fC[1]-1==fC[2]-2==fC[3]-3) and (fC[4]-1==fC[3] or fC[4]-12==fC[0])) else fC.append(5)
    elif ((fC[0] == fC[1]-1 == fC[2]-2 == fC[3]-3) and (fC[4]-1 == fC[3] or fC[4]-12 == fC[0])): fC.append(4) # straight
    elif fC[1]==fC[2]==fC[3] and (fC[0]==fC[1] or fC[3]==fC[4]): fC.extend([7, fC[0], fC[4]]) if fC[0]==fC[1] else fC.extend([7, fC[4], fC[0]]) # quads
    elif fC[0]==fC[1]==fC[2] and fC[3]==fC[4]: fC.extend([6, fC[0], fC[4]]) # boat, high set full of low pair
    elif fC[0] == fC[1] and fC[2] == fC[3] == fC[4]: fC.extend([6, fC[4], fC[0]]) # boat, low set full of high pair
    elif fC[0]==fC[1]==fC[2]: fC.extend([3, fC[0], fC[4], fC[3]]) # trips, both kickers higher; other kicker-types of trips in next line
    elif fC[2]==fC[3] and (fC[1]==fC[2] or fC[3]==fC[4]): fC.extend([3, fC[1], fC[4], fC[0]]) if fC[1]==fC[2] else fC.extend([3, fC[2], fC[1], fC[0]])
    elif (fC[0]==fC[1] and (fC[2]==fC[3] or fC[3]==fC[4])) or (fC[1]==fC[2] and fC[3]==fC[4]): # two pair
        if fC[0]==fC[1] and fC[2]==fC[3]: fC.extend([2, fC[3], fC[1], fC[4]]) # kicker higher than both pairs
        else: fC.extend([2, fC[4], fC[1], fC[2]]) if fC[0]==fC[1] and fC[3]==fC[4] else fC.extend([2,fC[4],fC[1],fC[0]])
    elif fC[0]==fC[1] or fC[1]==fC[2]: fC.extend([1, fC[0], fC[4], fC[3], fC[2]]) if fC[0]==fC[1] else fC.extend([1, fC[1], fC[4], fC[3], fC[0]])
    elif fC[2]==fC[3] or fC[3]==fC[4]: fC.extend([1, fC[2], fC[4], fC[1], fC[0]]) if fC[2]==fC[3] else fC.extend([1, fC[3], fC[2], fC[1], fC[0]])
    return fC if len(fC) > 5 else fC + [0] # return hand, but first if we haven't appended anything else note that it's just a high card hand

while True: # keep letting the user enter hands as long as they want to
    cards = raw_input("Enter the cards in a format like this: KhQh AsJs 5c6dTh4dJd ")
    cards = cards.replace("T", ":").replace("J", ";").replace("Q", "<").replace("K", "=").replace("A", ">")
    listOfCards = (",".join(str(ord(card)) for card in cards)).split(',')
    c = [ int(item) for item in listOfCards ]
    p1H = getBestFrom7([c[0], c[2], c[10], c[12], c[14], c[16], c[18]], [c[1], c[3], c[11], c[13], c[15], c[17], c[19]])
    p2H = getBestFrom7([c[5], c[7], c[10], c[12], c[14], c[16], c[18]], [c[6], c[8], c[11], c[13], c[15], c[17], c[19]])
    ranks = ["just a high card","one pair","two pair","trips","a straight","a flush","a boat","quads","a straight flush"]
    playerOneWins = firstHandIsBetter(p1H, p2H)
    if playerOneWins is None: print "The players chop, with " + ranks[p1H[5]]
    else: print 'Player %s wins, with ' % (1 if playerOneWins else 2) + (ranks[p1H[5]] if playerOneWins else ranks[p2H[5]])

    # When it prints out the players' cards, the first five characters are the hand itself, and then it says the hand's rank.
    #  Basically, the first number is the first relevant card, the second number is the second one, etc. More specifically:
        #  If we have a flush or just a high card, we need to check all 5 cards anyway, so we don't need any additional numbers.
        #  If we have one pair, we need all three kickers, so there's the value of the pair + three more kickers
        #  If we have two pair, we have the high pair, then the low pair, then the kicker.
        #  If we have trips, we have the trips card, then the first kicker, then the second kicker.
        #  If we have straight or straight flush, we only need to check the highest card, so there are no additional numbers.
        #  If we have a boat, we have one number for the trips, then another number for the pair.
        #  If we have quads, we have the quads card, then the kicker.
    for poop in range(len(p1H)): p1H[poop] -= 48 if poop != 5 else -51  # big number to make the output more legible
    for peep in range(len(p2H)): p2H[peep] -= 48 if peep != 5 else -51  # this is just changing the hand rank number
    r = ["highCard", "pair-", "2pair-", "trips-", "straight", "flush", "boat", "quads-", "straightFlush"]
    print " Player 1's best hand: " + " ".join(str(x) for x in p1H).replace("10","T").replace("11","J").replace("12","Q").replace("13","K").replace("14","A").replace("51",r[0]).replace("52 ",r[1]).replace("53",r[2]).replace("54",r[3]).replace("55",r[4]).replace("56",r[5]).replace("57",r[6]).replace("58",r[7]).replace("59",r[8])
    print " Player 2's best hand: " + " ".join(str(x) for x in p2H).replace("10","T").replace("11","J").replace("12","Q").replace("13","K").replace("14","A").replace("51",r[0]).replace("52 ",r[1]).replace("53",r[2]).replace("54",r[3]).replace("55",r[4]).replace("56",r[5]).replace("57",r[6]).replace("58",r[7]).replace("59",r[8]) + "\n"
