class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while i+1 != nums[i]:
                if nums[i] == nums[nums[i]-1]:
                    break
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        i = 0
        while i <len(nums):
            if i+1 != nums[i]:
                ans.append(nums[i])
            i+=1

        return ans