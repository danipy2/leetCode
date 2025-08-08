class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = set()
        def subset(arr,ind):
            t = tuple(sorted(arr).copy())
            if t not in s:
                s.add(t)
                ans.append(arr.copy())
            if ind>= len(nums):
                return 
            
            arr.append(nums[ind])
            subset(arr,ind+1)
            arr.pop()
            subset(arr,ind+1)
        subset([],0)
        return ans