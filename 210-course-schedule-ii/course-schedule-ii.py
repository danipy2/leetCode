class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [0 for i in range(numCourses)]
        prereq = [[] for i in range(numCourses)]
        for l,r in prerequisites:
            prereq[r].append(l) 
            req[l] += 1
        output = []
        i = 0 
        cond = True
        while cond:
            cond = False
            for i in range(len(req)):
                if req[i] == 0:
                    req[i] = -1
                    output.append(i)
                    for j in prereq[i]:
                        req[j] -= 1
                    cond = True
        if len(output) != numCourses:
            return []
        return output

                
        
