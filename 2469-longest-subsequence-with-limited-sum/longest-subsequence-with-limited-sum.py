class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        ans = []
        
        for i in range(len(queries)):
            l = 0
            r = len(nums)-1
            found = False
            while(l<=r):
                mid = (r+l)//2
                if nums[mid] > queries[i] and (mid==0 or nums[mid-1]<=queries[i]):
                    found = True
                    ans.append(mid)
                    break
                elif nums[mid] >queries[i]:
                    r = mid -1
                else:
                    l = mid +1
            if found == False:
                ans.append(l)
        return ans
                    