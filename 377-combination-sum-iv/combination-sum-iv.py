class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        tab = [0]*(target+1)
        tab[0] = 1
        for j in range(1, target + 1):   
            for num in nums:              
                if j >= num:
                    tab[j] += tab[j - num]
        return tab[target]


                
