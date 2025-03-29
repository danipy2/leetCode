class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        out = [0 for i in deck]
        st = []
        curr = -1
        q = deque()
        for i in range(len(deck)):
            q.append(i)
        deck.sort()
        for i in range(len(deck)):
            out[q.popleft()] = deck[i]
            if q:
                q.append(q.popleft())
        return out
