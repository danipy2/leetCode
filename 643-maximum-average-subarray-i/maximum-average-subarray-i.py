class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxtotal = sum(nums[:k])
        total = maxtotal
        for i in range(k,len(nums)):
            total += (nums[i]-nums[i-k])
            if maxtotal <total:
                maxtotal = total
        return maxtotal/k


            

        
            
            