class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic = Counter(list(s))
        m1 = 0
        m2 = 0
        v = {"a","e","i","o","u"}
        for i in dic:
            if i in v:
                m1 = max(m1,dic[i])
            else:
                m2 = max(m2,dic[i])
        return m1+m2