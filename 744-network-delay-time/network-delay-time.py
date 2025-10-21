class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        prv = [float("inf") ] * (n+1)
        prv[k] = 0
        for i in range(n-1):
            cond = False
            for u,v,w in times:
                minm = min(prv[v],prv[u]+w)
                if  minm != prv[v]:
                    prv[v] = minm
                    cond = True
            if not cond:
                break
        maxm = max(prv[1:])
        return  maxm if maxm != float("inf") else -1