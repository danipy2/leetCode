class Solution:
    def frequencySort(self, s: str) -> str:
        sm = Counter(s)
        so = sorted(sm.keys(),key=lambda x:(-sm[x],s.index(x)))
        return "".join([i*sm[i] for i in so])