class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        last = len(nums)-1
        count = 0
        while(last>0):
            for i in range(last):
                if (i*last)%k:
                    continue    
                if nums[i] == nums[last]:
                    count += 1
            last -=1
        return count

            

        