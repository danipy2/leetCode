class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 1
        stotal = 0
        total = 0
        for i in arr:
            total += i
            if total%2:
                stotal += even
                odd+=1
            else:
                stotal += odd
                even +=1
        return stotal%(10**9+7)
                