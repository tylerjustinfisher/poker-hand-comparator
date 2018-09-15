def firstHandIsBetter(h1, h2): # given two hands, with the 5 cards + rank + relevant kicker details, say which wins
    if h1[5] != h2[5]: return h1[5] > h2[5] # different ranks
    if h1[5]==8 or h1[5]==4: return h1[2] > h2[2] if h1[2] != h2[2] else None # SF or straight: check middle card
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
    if fS.count(fS[0])==len(fS): return (fC + [8]) if fC[0]==fC[1]-1==fC[2]-2==fC[3]-3 and (fC[4]-1==fC[3] or fC[4]-12==fC[0]) else (fC+[5])
    if fC[0]==fC[1]-1==fC[2]-2==fC[3]-3 and (fC[4]-1==fC[3] or fC[4]-12==fC[0]): return (fC+[4]) # straight; consider ace as high or low
    if fC[1]==fC[2]==fC[3] and (fC[0]==fC[1] or fC[3]==fC[4]): return (fC+[7]+[fC[0]]+[fC[4]]) if fC[0]==fC[1] else (fC+[7]+[fC[4]]+[fC[0]])
    if (fC[0]==fC[1]==fC[2] and fC[3]==fC[4]) or (fC[0]==fC[1] and fC[2]==fC[3]==fC[4]): return (fC+[6]+[fC[0]]+[fC[4]]) if fC[0]>fC[4] else (fC+[6]+[fC[4]]+[fC[0]])
    if fC[0]==fC[1]==fC[2] or fC[1]==fC[2]==fC[3] or fC[2]==fC[3]==fC[4]: return (fC+[3]+[fC[0]]+[fC[4]]+[fC[3]]) if fC[0]==fC[1] else (fC+[3]+[fC[2]]+[fC[1]]+[fC[0]]) if fC[3]==fC[4] else (fC+[3]+[fC[1]]+[fC[4]]+[fC[0]])
    if (fC[0]==fC[1] and (fC[2]==fC[3] or fC[3]==fC[4])) or (fC[1]==fC[2] and fC[3]==fC[4]): return (fC+[2]+[fC[3]]+[fC[1]]+[fC[4]]) if fC[3]!=fC[4] else (fC+[2]+[fC[4]]+[fC[1]]+[fC[0]]) if fC[0]!=fC[1] else (fC+[2]+[fC[4]]+[fC[1]]+[fC[2]])
    return (fC+[1]+[fC[0]]+[fC[4]]+[fC[3]]+[fC[2]]) if fC[0]==fC[1] else (fC+[1]+[fC[1]]+[fC[4]]+[fC[3]]+[fC[0]]) if fC[1]==fC[2] else (fC+[1]+[fC[2]]+[fC[4]]+[fC[1]]+[fC[0]]) if fC[2]==fC[3] else (fC+[1]+[fC[3]]+[fC[2]]+[fC[1]]+[fC[0]]) if fC[3]==fC[4] else (fC+[0])
c, ranks= [ int(item) for item in ((",".join(str(ord(card)) for card in (raw_input("Input like: KhQh AsJs 5c6dTh4dJd ").replace("T",":").replace("J",";").replace("Q","<").replace("K","=").replace("A",">")))).split(',')) ], ["just a high card","one pair","two pair","trips","a straight","a flush","a boat","quads","a straight flush"]
p1H, p2H = getBestFrom7([c[0], c[2], c[10], c[12], c[14], c[16], c[18]], [c[1], c[3], c[11], c[13], c[15], c[17], c[19]]), getBestFrom7([c[5], c[7], c[10], c[12], c[14], c[16], c[18]], [c[6], c[8], c[11], c[13], c[15], c[17], c[19]])
print "The players chop, with " + ranks[p1H[5]] if firstHandIsBetter(p1H, p2H) is None else 'Player %s wins, with ' % (1 if firstHandIsBetter(p1H, p2H) else 2) + (ranks[p1H[5]] if firstHandIsBetter(p1H, p2H) else ranks[p2H[5]])
