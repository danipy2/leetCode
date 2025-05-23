class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix  = [0]
        for i in arr:
            prefix.append(prefix[-1]^i)
        ans = []
        for left ,right in queries:
            ans.append(prefix[right+1]^prefix[left])
        return ans
