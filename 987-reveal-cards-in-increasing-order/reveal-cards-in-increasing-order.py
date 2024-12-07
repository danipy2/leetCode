class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        myqueue = deque()
        if len(deck) <= 2:
            return deck
        deck.sort()
        myqueue.append(deck[-2])
        myqueue.append(deck[-1])
        deck.pop()
        deck.pop()
        while deck:
            temp = myqueue.pop()
            temp1 = deck.pop()
            myqueue.append(temp1)
            myqueue.append(temp)
            while myqueue[0] != temp1:
                myqueue.append(myqueue.popleft())
        return list(myqueue)