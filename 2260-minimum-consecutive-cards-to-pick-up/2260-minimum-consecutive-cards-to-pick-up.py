class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        myset = set()
        max1 = len(cards)+1
        left = 0
        for i in range(len(cards)):
            leng = len(myset)
            myset.add(cards[i])
            if leng == len(myset):
                while(cards[left]!=cards[i] and left<i):
                    myset.remove(cards[left])
                    left+=1
                if max1 > i-left+1:
                    max1 = i-left+1
                left +=1

        if max1 <= len(cards):
           return max1 
        return -1