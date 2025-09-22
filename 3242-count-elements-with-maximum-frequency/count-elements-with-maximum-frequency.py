class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = [0] * 100
        for i in nums:
            arr[i-1]+=1
        c = Counter(arr)
        m = 0
        
        for i in c:
            if i:
                m = max(m,i)
        return c[m] *m