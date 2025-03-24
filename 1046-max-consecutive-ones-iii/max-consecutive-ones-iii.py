class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        queue = deque()
        i = 0
        l = 0
        maxm = 0
        while i<len(nums):
            if nums[i] == 0:
                queue.append(i)
            if len(queue) >k:
                l =  queue.popleft() +1
            maxm = max(maxm,i-l+1)
            i+=1
        return maxm

