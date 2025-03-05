class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x:x[1])
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                count+=1
                intervals[i][1] = intervals[i-1][1]
        return count