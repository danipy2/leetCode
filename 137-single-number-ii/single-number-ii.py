class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total  = 0
            for j in nums:
                if j <0:
                    j  &= (2**32-1)
                total +=( j>>i ) & 1
            total %= 3
            ans |= total << i
        if ans >= (2**31):
            return ans-(2**32)
        return ans