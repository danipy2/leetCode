class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        myd = {}
        l = 0
        maxm = 0
        count = 0
        for i in range(len(fruits)):
            if fruits[i] in myd and myd[fruits[i]]:
                myd[fruits[i]]+=1
            else:
                myd[fruits[i]]  = 1
                count+=1
            if count >= 3:
                if myd[fruits[l]] == 1:
                    count-=1
                myd[fruits[l]]-=1 
                l+=1 
            maxm = max(maxm,i-l+1)
        return maxm
