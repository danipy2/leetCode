class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(arr,ind,t):
            if t == target:
                ans.append(arr[:])
                return 
            if ind == len(candidates) or t>target:
                return
            arr.append(candidates[ind])
            if candidates[ind]+t<=target:
                backtrack(arr,ind,t+candidates[ind])
            arr.pop()
            backtrack(arr,ind+1,t)
        backtrack([],0,0)
        return ans
            