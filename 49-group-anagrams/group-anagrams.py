class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i in range(len(strs)):
            w = strs[i]
            print(w)
            s = sorted(w)
            s = "".join(s)
            if s in d:
                ans[d[s]].append(w)
            else:
                d[s] = len(ans)
                ans.append([w])
        return ans

