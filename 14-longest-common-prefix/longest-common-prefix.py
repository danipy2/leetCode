class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind = 0 
        ans = ""
        while True:
            for i in range(1,len(strs)):
                if ind>=len(strs[i-1]) or ind>= len(strs[i])  or strs[i][ind]!=strs[i-1][ind]:
                    return ans
            if ind>=len(strs[0]) or not strs:
                return ans
            ans+=strs[0][ind]
            ind+=1
        