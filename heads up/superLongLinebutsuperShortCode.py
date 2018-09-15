def firstHandIsBetter(h1, h2): # given two hands, with the 5 cards + rank + relevant kicker details, say which wins
    if h1[5]!=h2[5] or h1[5]==8 or h1[5]==4: return h1[5]>h2[5] if h1[5]!=h2[5] else h1[2]>h2[2] if h1[2]!=h2[2] else None
    if h1[5]==5 or h1[5]==0: # flush or high card: check all five cards
        for x in range(5):
            if h1[4 - x] != h2[4 - x]: return h1[4 - x] > h2[4 - x]
        return None # chop
    for y in range(6,10):
        if h1[y]!=h2[y] or len(h1)==y+1: return h1[y]>h2[y] if h1[y]!=h2[y] else None
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
def getHandRankFromFiveCards(z, fS): # given 5 cards, determine what the rank of the hand is and add kicker info to it
    if fS.count(fS[0])==len(fS): return (z + [8]) if z[0]==z[1]-1==z[2]-2==z[3]-3 and (z[4]-1==z[3] or z[4]-12==z[0]) else (z+[5])
    return (z+[4]) if z[0]==z[1]-1==z[2]-2==z[3]-3 and (z[4]-1==z[3] or z[4]-12==z[0]) else (z+[7]+[z[0]]+[z[4]]) if z[0]==z[1]==z[2]==z[3] else (z+[7]+[z[4]]+[z[0]]) if z[1]==z[2]==z[3]==z[4] else (z+[6]+[z[0]]+[z[4]]) if (z[0]==z[1]==z[2] and z[3]==z[4]) else (z+[6]+[z[4]]+[z[0]]) if (z[0]==z[1] and z[2]==z[3]==z[4]) else (z+[3]+[z[0]]+[z[4]]+[z[3]]) if z[0]==z[1]==z[2] else (z+[3]+[z[1]]+[z[4]]+[z[0]]) if z[1]==z[2]==z[3] else (z+[3]+[z[2]]+[z[1]]+[z[0]]) if z[2]==z[3]==z[4] else (z+[2]+[z[3]]+[z[1]]+[z[4]]) if (z[0]==z[1] and z[2]==z[3]) else (z+[2]+[z[4]]+[z[1]]+[z[0]]) if (z[1]==z[2] and z[3]==z[4]) else (z+[2]+[z[4]]+[z[1]]+[z[2]]) if (z[0]==z[1] and z[3]==z[4]) else (z+[1]+[z[0]]+[z[4]]+[z[3]]+[z[2]]) if z[0]==z[1] else (z+[1]+[z[1]]+[z[4]]+[z[3]]+[z[0]]) if z[1]==z[2] else (z+[1]+[z[2]]+[z[4]]+[z[1]]+[z[0]]) if z[2]==z[3] else (z+[1]+[z[3]]+[z[2]]+[z[1]]+[z[0]]) if z[3]==z[4] else (z+[0])
c, ranks= [ int(item) for item in ((",".join(str(ord(card)) for card in (raw_input("Input like: KhQh AsJs 5c6dTh4dJd ").replace("T",":").replace("J",";").replace("Q","<").replace("K","=").replace("A",">")))).split(',')) ], ["just a high card","one pair","two pair","trips","a straight","a flush","a boat","quads","a straight flush"]
p1H, p2H = getBestFrom7([c[0], c[2], c[10], c[12], c[14], c[16], c[18]], [c[1], c[3], c[11], c[13], c[15], c[17], c[19]]), getBestFrom7([c[5], c[7], c[10], c[12], c[14], c[16], c[18]], [c[6], c[8], c[11], c[13], c[15], c[17], c[19]])
print "The players chop, with " + ranks[p1H[5]] if firstHandIsBetter(p1H, p2H) is None else 'Player %s wins, with ' % (1 if firstHandIsBetter(p1H, p2H) else 2) + (ranks[p1H[5]] if firstHandIsBetter(p1H, p2H) else ranks[p2H[5]])
