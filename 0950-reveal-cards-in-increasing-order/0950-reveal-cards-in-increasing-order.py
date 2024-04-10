import math
class Solution:
    def deckRevealedIncreasing(self,deck):
        mylist = sorted(deck)
        length = len(deck)
        if length < 3:
            return deck
        newlist = mylist[length - 2:length]
        mylist = mylist[:length - 2]
        for i in range(length - 3, -1, -1):
            newlist.insert(0, newlist[-1])
            newlist.pop()
            newlist.insert(0, mylist[i])
        return newlist
