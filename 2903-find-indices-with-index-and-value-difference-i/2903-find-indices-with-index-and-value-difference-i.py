class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        right = len(nums)-1
        for i in range(len(nums)):
            j = i+indexDifference
            while(j<=right):
                if abs(nums[j]-nums[i]) >= valueDifference:
                    return [i,j]
                j+=1
        return [-1,-1]
            
        