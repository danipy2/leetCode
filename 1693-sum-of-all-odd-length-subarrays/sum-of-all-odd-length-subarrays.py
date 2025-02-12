class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for i, val in enumerate(arr):
            left = i + 1         
            right = n - i        
            odd_count = ((left + 1) // 2) * ((right + 1) // 2) + (left // 2) * (right // 2)
            total += val * odd_count
        return total

