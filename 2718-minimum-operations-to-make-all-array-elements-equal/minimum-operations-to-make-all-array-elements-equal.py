class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        p = [0]
        for i in nums:
            p.append(p[-1]+i)
        output = []
        for i in queries:
            ind = 0
            l = 0
            r = len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == i:
                    ind = mid
                    break
                elif nums[mid]>i:             
                    r = mid-1
                else:
                    l=mid+1
            if l>r:
                ind = l-1
            less =( i *(ind+1)) - p[ind+1]
            gre =( p[-1]-p[ind+1]) - (i *(len(p)-ind-2))
            output.append(gre+less)
        return output
        