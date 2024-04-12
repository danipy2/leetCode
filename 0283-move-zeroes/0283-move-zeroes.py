class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count =0
        i = 0
        while (i<len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                count +=1
            else:
                i += 1
        for i in range(count):
            nums.append(0)

