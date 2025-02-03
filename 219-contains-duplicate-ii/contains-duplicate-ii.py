class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset = set()
        l = 0
        for i in range(len(nums)):
            while(i-l>k):
                myset.remove(nums[l])
                l+=1
            if nums[i] in myset:
                return True
            myset.add(nums[i])
        return False
            