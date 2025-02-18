class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        for i in range(len(nums)-1, -1, -1):
            if output:
                output.append(output[-1] * nums[i])
            else:
                output.append(nums[i])
        pre = 1
        for i in range(len(nums)-1,0,-1):
            post = output[i-1]
            output[i] = (pre*post)
            pre *= nums[len(nums)-1-i]
        output[0] = pre
        output.reverse()
        
        return output
            

