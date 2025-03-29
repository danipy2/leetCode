class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        out = [0 for i in deck]
        st = []
        curr = -1
        myset = set()
        for i in range(len(deck)):
            while curr%len(deck) in myset:
                curr+=1
            curr+=1
            while curr%len(deck) in myset:
                curr+=1

            st.append(curr%len(deck))
            myset.add(curr%len(deck))
        deck.sort()
        for i in range(len(deck)):
            out[st[i]] = deck[i]
        return out
