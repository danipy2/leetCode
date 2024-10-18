class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        nums = []
        nums2 = []
        for i in range(1,n+1):
            if n%i==0 :
                if len(nums)==0 or n//i > nums[-1]:
                    nums.append(i)
                if  n//i > i:
                    nums2.append(n//i)
            else:
                if i+1 >= nums2[-1] :
                    break
        if k > (len(nums) + len(nums2)):
            return -1
        else:
            if k <= len(nums):
                return nums[k-1]
            else:
                return nums2[(k-len(nums))*-1] 
