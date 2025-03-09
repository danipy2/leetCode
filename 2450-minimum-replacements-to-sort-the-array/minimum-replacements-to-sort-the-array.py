class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2,-1,-1):
                k = math.ceil(nums[i] / nums[i+1])
                count += (k - 1)
                nums[i] = nums[i] // k
        return count