class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = deque()
        
        arr = [[]for i in range(n)]
        for i in range(len(manager)):
            if manager[i] != -1:
                arr[manager[i]].append(i)
        ans = informTime[headID]
        q.append([arr[headID],ans])
        finalans = ans
        while q:
            ar,t = q.popleft()
            finalans = max(finalans,t)
            for i in ar:
                q.append([arr[i],t+ informTime[i]])
        return finalans