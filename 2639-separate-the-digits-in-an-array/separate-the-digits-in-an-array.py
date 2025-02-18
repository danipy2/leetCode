class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            newarr= []
            x = 1
            while nums[i]>=x:
                x*=10
                n = nums[i]%x

                nums[i] -=(n/(x/10) )
                newarr.append(n/(x/10))
            while newarr:
                arr.append(int(newarr.pop()))
        return arr