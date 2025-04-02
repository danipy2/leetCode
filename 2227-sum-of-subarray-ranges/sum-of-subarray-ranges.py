class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        left1 = [-1] * len(nums)
        right1 = [n] * len(nums)
        left2 = [-1] * len(nums)
        right2 = [n] * len(nums)
        stack1 = []
        stack2 = []
        for i in range(len(nums)):
            while stack1 and nums[stack1[-1]]>= nums[i]:
                right1[stack1.pop()] = i
            if stack1:
                left1[i] = stack1[-1]
            stack1.append(i)
            
            while stack2 and nums[stack2[-1]] <= nums[i]:
                right2[stack2.pop()] = i
            if stack2:
                left2[i] = stack2[-1]
            stack2.append(i)
        result1 = sum((i - left1[i]) * (right1[i] - i) * nums[i] for i in range(len(nums)))
        result2 = sum((i - left2[i]) * (right2[i] - i) * nums[i] for i in range(len(nums)))

        return (result2-result1) 

                