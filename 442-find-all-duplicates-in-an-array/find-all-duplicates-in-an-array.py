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
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])

        return ans