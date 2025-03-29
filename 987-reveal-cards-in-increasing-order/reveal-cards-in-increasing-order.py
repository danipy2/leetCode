class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        out = [0 for i in deck]
        deck.sort()
        curr = 0
        out[0] = deck[0]
        for i in deck[1:]:
            steps = 1
            while True:
                if out[curr%len(out)]==0:
                    if steps:
                        steps-=1
                    else:
                        out[curr%len(out)] = i
                        break
                curr+=1
        return out
