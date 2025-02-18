class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        arr = [i for i in nums]
        for i in range(len(nums)): 
            arr[i] =  nums[(nums[i]+i)%len(nums)]
        return arr