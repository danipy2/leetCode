class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        arr = [-1,-1]
        for i in range(1,len(nums)+1):
            if i not in s:
                arr[1] =  i
            elif s[i] == 2:
                arr[0] = i
        return arr

