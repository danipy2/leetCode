class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        minm = -1
        maxm = -1
        count = 0
        for i in range(len(intervals)):
            if intervals[i][0] > minm and intervals[i][0]<=maxm:
                    count+=1
                    
                    minm = maxm
                    maxm = intervals[i][1]
                    if minm ==maxm:
                        minm-=1
            elif intervals[i][0] > minm:
                count+=2
                minm = intervals[i][1]-1
                maxm = intervals[i][1]
                
        return count