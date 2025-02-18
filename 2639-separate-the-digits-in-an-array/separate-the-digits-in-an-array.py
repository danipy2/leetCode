class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            j = str(i)
            for k in j:
                arr.append(int(k))
        return arr