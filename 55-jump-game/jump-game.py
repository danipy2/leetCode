class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-2,-1,-1):
            if count:
                if (nums[i]-1)>=count:
                    count=0
                else:
                    count+=1
            else:
                if nums[i]==0:
                    count+=1
        if count:
            return False
        return True
