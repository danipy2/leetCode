class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        prv = [float("inf") ] * (n)
        prv[k-1] = 0
        for i in range(n-1):
            curr = prv[:]
            for u1,v1,w1 in times:
                u,v,w = u1-1,v1-1,w1
                curr[v] = min(curr[v],prv[u]+w)
            prv = curr
        maxm = max(prv)
        return  maxm if maxm != float("inf") else -1