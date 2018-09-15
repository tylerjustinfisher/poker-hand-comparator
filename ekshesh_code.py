from sets import Set
def compareboards( board1, board2, suits1, suits2, pr):
    list,  hand1,  hand2 = [ "Straight flush", "Quads", "Full house", "Flush", "Straight", "Three of a kind", "Two Pair", "A Pair", "High Hand"], handtype(Set(suits1),Set(board1), sorted(board1)), handtype(Set(suits2), Set(board2),sorted(board2))
    if hand1 != hand2 and pr: print " PLayer 1 wins with a " + list[hand1] if hand1 < hand2 else  "PLayer 2 wins with " + list[hand2]
    elif hand2 != hand1:  return (board2, suits2) if hand2 < hand1 else ( board1, suits1)
    else:
        list1sorted, list2sorted =  sorted(sorted(board1, reverse = True), key = board1.count, reverse = True), sorted(sorted(board2, reverse = True), key = board2.count, reverse = True) ;
        if (hand1 ==4) and (list1sorted != list2sorted and (list1sorted == [14, 5, 4, 3, 2] or list2sorted == [14, 5, 4, 3, 2])) and pr: print " PLayer 2 wins with a  " + list[hand2]  if list1sorted== [14, 5, 4, 3, 2] else " Player 1 wins with a " + list[hand2]
        if (hand1 ==4) and (list1sorted != list2sorted and (list1sorted == [14, 5, 4, 3, 2] or list2sorted == [14, 5, 4, 3, 2])): return board2, suits2 if (list1sorted==[14, 5, 4, 3, 2]) else (board1, suits1)
        for i in range(len(list1sorted)):
            if (list1sorted[1] != list2sorted[i] or i == len(list1sorted) -1) and pr:  print " PLayer 1 wins with a " + list[hand1] if list1sorted[i] > list2sorted[i]  else " Player 2 wins with a " + list[hand2] if list1sorted[i] < list2sorted[i]  else  "The Players Chop with a " + list[hand1]
            if  (list1sorted[1] != list2sorted[i] or i == len(list1sorted) -1): return (board1, suits1) if list1sorted[i] > list2sorted[i] else (board2, suits2)
def winner(sevencards, suits, besthand, besthandsuits):
    for i in range( 6):
        for j in range(i +1, 7):
            besthand, besthandsuits = compareboards(besthand, sevencards[ :i] + sevencards[i +1: j] + sevencards[j +1: 7], besthandsuits, suits[ :i] + suits[i +1: j] + suits[j +1: 7],  False)
    return besthand, besthandsuits
def handtype(setsuits, setcards, sortedcards):
    if len(setcards) == 1 and sortedcards[-1] - sortedcards[0] == 4: return 0
    if len(setcards) == 2 and max([sortedcards.count(i) for i in setcards]) == 4: return 1
    elif len(setcards)== 2 and max([sortedcards.count(i) for i in setcards]) == 3: return 2
    elif len(setsuits) == 1 : return 3
    elif len(setcards) == 5 and (sortedcards[-1] - sortedcards[0] ==4 or sortedcards == [2, 3, 4, 5, 14]): return 4
    elif len(setcards) == 3 and max([sortedcards.count(i) for i in setcards]) == 3: return 5
    elif len(setcards) == 3 and max([sortedcards.count(i) for i in setcards]) == 2: return 6
    elif len(setcards) == 4: return 7
    else: return 8
def handcomparator(hand1, hand2, board, suits1, suits2, suitsboard, dic):
     hand1, hand2, board = [dic[t] if t in dic else int(t) for t in hand1], [dic[t] if t in dic else t for t in hand2],  [dic[t] if t in dic else int(t) for t in board]
     bh, bs =  winner(hand1 + board, suits1 + suitsboard, [2,3,4,5,7], ["c", "c",  "d", "d","s"])
     bh2, bs2 = winner(hand2 + board, suits2 + suitsboard, [2,3,4,5,7], ["c", "c" ,"d", "d","s"])
     compareboards(bh, bh2, bs, bs2, True )
handcomparator([8, 6], [8, 6], ["A", 8, "K", 4, 6], ["c", "c"], ["s", "d"], ["h", "c", "s", "c", "d"], {"T" : 10, "J": 11, "Q" : 12, "K" : 13, "A": 14})
