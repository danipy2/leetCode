class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxm = 0
        while l < r:
            maxm = max(maxm,min(height[l],height[r])*(r-l))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return maxm
        
            