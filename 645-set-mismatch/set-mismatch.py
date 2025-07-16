class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0 for i in nums]
        for i in nums:
            arr[i-1] +=1
        ans = [i+1 for i in range(len(arr)) if arr[i] ==0 or arr[i]==2]
        if arr[ans[0]-1] == 0:
            ans[0],ans[1] = ans[1],ans[0]
        
        return ans