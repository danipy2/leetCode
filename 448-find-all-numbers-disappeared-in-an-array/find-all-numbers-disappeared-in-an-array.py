class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in nums:
            arr[i-1] +=1
        ans = [i+1 for i in range(len(nums)) if arr[i]==0]
        return ans

        