class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = bisect_left(nums,target)
        return ind if ind<len(nums) and nums[ind] == target else -1