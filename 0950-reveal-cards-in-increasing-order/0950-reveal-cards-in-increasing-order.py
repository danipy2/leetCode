class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        mylist = sorted(deck)
        if len(deck) < 3:
            return deck
        newlist = mylist[len(mylist) - 2:len(mylist)]
        mylist = mylist[:len(mylist) - 2]
        while (len(mylist)):
            newlist.insert(0, newlist[-1])
            newlist.pop()
            newlist.insert(0, mylist[-1])
            mylist.pop()
        return newlist



        