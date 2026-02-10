class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        c = Counter(nums)
        s = sorted(nums)
        v = set()
        count = 0
        for i in s:
            if i not in v:
                d[i] = count
                count += c[i]
            v.add(i)
        nums = [d[i] for i in nums]
        return nums
