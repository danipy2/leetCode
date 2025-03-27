class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        myset = set()
        myset.add(0)
        count = 0
        total = 0
        for i in nums:
            total += i
            if total-target in myset:
                myset = set()
                myset.add(0)
                total = 0
                count+=1
            else:
                myset.add(total)

        return count