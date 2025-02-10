class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
      remainder={}
      total=0
      i=0
      while(i<len(nums)):
        total+=nums[i]
        r=total%k
        if r in remainder and i-remainder[r]>1:
            return True
        elif i>=1 and r==0:
            return True
        else:
            if  r not in remainder:
                remainder[r]=i
            i+=1
    
      return False