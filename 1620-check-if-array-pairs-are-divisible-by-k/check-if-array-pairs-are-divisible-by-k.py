class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = [0 ] * k
        for i in arr:
            val = k- (i%k)
            if val==k:
                continue
            if d[val]:
                d[val]-=1
            else:
                d[i%k] +=1
        
        return sum(d) ==0