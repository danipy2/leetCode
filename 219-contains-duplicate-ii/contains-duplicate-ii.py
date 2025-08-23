class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sset = set()
        r = 0
        l = 0
        if k == 0:
            return False
        while r< len(nums):
            while r<len(nums) and len(sset) <= k:
                if nums[r] in sset:
                    return True
                sset.add(nums[r])   
                r+=1
            if sset:
                sset.remove(nums[l])
            l+=1
        return False