class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind = 0 
        ans = ""
        while True:
            if ind >= len(strs[0]):
                return ans
            letter = strs[0][ind]
            for i in range(1,len(strs)):
                if  ind>= len(strs[i])  or strs[i][ind]!=letter:
                    return ans
            ans+=strs[0][ind]
            ind+=1
        