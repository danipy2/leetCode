class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [[nums[0],nums[0]]]
        minm = nums[0]
        for i in range(1,len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            else:
                if i > 1:
                    r = len(stack)-1
                    while r>=0:
                        if stack and  stack[r][1] < nums[i]:
                            return True
                        r-=1
                stack.append([nums[i],minm])
            minm = min(minm,nums[i])
        return False


            
            
            