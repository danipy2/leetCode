class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        add = 0
        contain = nums[0]
        for i in nums:
            if i != contain:
                add+=1
                contain = i
            total += add
        return total