class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [0 for i in range(numCourses)]
        prereq = [[] for i in range(numCourses)]
        for l,r in prerequisites:
            prereq[r].append(l) 
            req[l] += 1
        output = []
        qeue = deque()
        for i in range(len(req)):
            if req[i] == 0:
                output.append(i)
                qeue.append(i)
        while qeue:
            n = qeue.popleft()
            for i in prereq[n]:
                req[i] -= 1
                if req[i] == 0:
                    qeue.append(i)
                    output.append(i)
        if len(output) != numCourses:
            return []
        return output

                
        
