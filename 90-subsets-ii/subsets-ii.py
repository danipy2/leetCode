class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def subset(arr,prev,ind):          
            if ind>= len(nums):
                ans.append(arr.copy())
                return 
            if  prev+1==ind or nums[ind-1] != nums[ind]:
                arr.append(nums[ind])
                subset(arr,ind,ind+1)
                arr.pop()
            subset(arr,prev,ind+1)
        subset([],-1,0)
        return ans