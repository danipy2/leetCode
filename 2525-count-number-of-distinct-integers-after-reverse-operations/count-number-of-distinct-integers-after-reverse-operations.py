class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        revnum=[int(str(i)[::-1]) for i in nums]
        nums+=revnum
        return len(set(nums))