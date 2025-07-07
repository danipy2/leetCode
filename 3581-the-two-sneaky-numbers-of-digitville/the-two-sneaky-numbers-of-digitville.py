class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [i for i,x in c.items() if x==2]