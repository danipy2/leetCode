class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        myd = {}
        l = 0
        maxm = 0
        for i in range(len(fruits)):
            if fruits[i] in myd:
                myd[fruits[i]]+=1
            else:
                myd[fruits[i]]  = 1
            if len(myd) >=3:
                if myd[fruits[l]] == 1:
                    del  myd[fruits[l]]
                else:
                    myd[fruits[l]]-=1 
                l+=1 
            maxm = max(maxm,i-l+1)
        return maxm
