class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        n  = 0
        for i in nums:
            if i in s:
                n = i
                break
            s.add(i)
        total = (len(nums) * (len(nums)+1))//2
        n2 = total -( sum(nums) - n)
        return [n,n2]