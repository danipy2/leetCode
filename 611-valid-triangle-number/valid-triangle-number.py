class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        lst = max(nums)+2
        lgth = len(nums)
        arr = [lgth] *lst
        for i in range(len(nums)):
            if arr[nums[i]] == lgth:
                arr[nums[i]] = i

        for i in range(len(arr)-2,-1,-1):
            if arr[i] == lgth:
                arr[i] = arr[i+1]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                add = nums[i]+nums[j]
                rindx = arr[min(add,len(arr)-1)]
                s = rindx - j-1
                if s>0:
                    count+=s
        return count
                    

