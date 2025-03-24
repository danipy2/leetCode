class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        l = 0
        maxm = 0
        count = 0
        while i<len(nums):
            if nums[i] == 0:
                count+=1
            while count >k and l<=i:
                if nums[l] == 0:
                    count -=1
                l+=1
            if l<=i:
                maxm = max(maxm,(i-l)+1) 
            i+=1
        return maxm

