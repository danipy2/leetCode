class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        for i in arr:
            val = k- (i%k)
            if val==k:
                continue

            if val in d:
                d[val]-=1
                if d[val] ==0:
                    del d[val]
            else:
                d[i%k] = d.get(i%k,0)+1
        if d:
            return False
        return True