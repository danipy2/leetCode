class Solution:
    def findComplement(self, num: int) -> int:
        total = 0
        for i in range(num.bit_length()):
            if num & (1 << i) == 0:
                total += 1 << i
        return total