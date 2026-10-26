class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = []
        for ind,value in enumerate(nums):
            arr.append((value,ind))
        arr.sort()

        l = 0
        r = len(nums)-1
        while l<r:
            total = arr[l][0] + arr[r][0] 
            if  total ==target:
                return [arr[l][1],arr[r][1]]
            elif total >target:
                r-=1
            else:
                l+=1
         
