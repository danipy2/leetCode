class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k =( k%(len(nums)))
        if k == 0:
            return
        i = 0
        temp = nums[0]
        count=0
        while (i<len(nums) and count<len(nums)):
            n = (i+k)%len(nums)
            t = nums[n]
            nums[n] = temp
            temp = t

            i = n
            count+=1
            if (k*count)%len(nums)==0 and   count % (len(nums)//k)==0:
                i+=1
                if i <len(nums):
                    temp = nums[i]
            elif count==len(nums):
                break
            


