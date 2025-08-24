class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        max_heap = []
        minm_heap = []
        i = 0 
        j = 0 
        s = SortedList([])
        while i <len(nums):
            while i < len(nums) and i-j <=indexDiff:
                val = nums[i]
                g = s.bisect_right(val)
                sm  = s.bisect_left(val)
                if g<len(s) and abs(s[g]-val) <= valueDiff:
                    return True
                if sm>0 and abs(val- s[sm-1]) <=valueDiff:
                    return True
                if sm<len(s) and abs(val-s[sm])<=valueDiff:
                    return True
                s.add(val)
                i+=1
                
            s.remove(nums[j])
            j+=1
        return False