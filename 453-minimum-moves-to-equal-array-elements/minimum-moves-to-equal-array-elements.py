class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        t = nums[-1]-nums[0]
        total = t
        for i in range(len(nums)-2,-1,-1):
            total+= (nums[i]-nums[0])
        return total