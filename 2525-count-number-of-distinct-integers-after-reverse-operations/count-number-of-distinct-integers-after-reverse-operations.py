class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        newset = set()
        total = 0
        for i in nums:
            j = str(i)
            newset.add(j)
            newset.add(j[::-1].lstrip('0'))
        return len(newset)