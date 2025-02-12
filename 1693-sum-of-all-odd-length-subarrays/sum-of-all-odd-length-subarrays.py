class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        left = 0
        p = [0 for i in range(len(arr)+1)]
        p[1] = arr[0]
        for i in range(1,len(arr)):
            p[i+1] = p[i] +arr[i]
        total = 0
        for i in range(1,len(p)):
            l = 0
            while l<i:
                if (i-l)%2:
                    total +=  p[i]-p[l]
                l+=1
        return total