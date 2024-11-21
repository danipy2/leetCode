class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i]+=1
        tot = 0
        n = 0
        i = 0
        while i <len(nums):
            while(count[n]):
                count[n]-=1
                nums[i] = n
                i+=1
            n+=1

        