class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        l = list(s)
        m = l[:]
        for i in range(len(l)):
            m[indices[i]] = l[i]
        return "".join(m)


