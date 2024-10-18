class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxm = right * min(height[right],height[0])
        while(left<right):
            if height[right] <height[left]:
                right-=1
            else:
                left+=1
            new = ((right-left) * min(height[right],height[left]))
            if new > maxm:
                maxm = new
        return maxm