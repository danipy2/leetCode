class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        visted = set()
        rednode = [[] for i in range(n)]
        bluenode = [[] for i in range(n)]
        for start,end in redEdges:
            rednode[start].append(end)
        for start,end in blueEdges:
            bluenode[start].append(end)
        q = deque()
        q.append((0,-1,0))
        while q:
            c,cl,d = q.popleft()
            if (c,cl) in visted:
                continue
            visted.add((c,cl))
            if ans[c] == -1:
                ans[c] = d
            
            if cl != 0:
                for i in rednode[c]:
                    t = (i,0,d+1)
                    q.append(t)
            if cl != 1:
                for i in bluenode[c]:
                    t = (i,1,d+1)
                    q.append(t)
        return ans