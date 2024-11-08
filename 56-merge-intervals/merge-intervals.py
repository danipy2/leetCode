class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=output[-1][1]:
                temp = [output[-1][0],max(output[-1][1],intervals[i][1])]
                j = -2
                output[-1] = temp
                while(j*-1 <=len(output) and temp[0]<=output[j][1]):
                    output[j] = [output[-1][0],max(output[-1][1],intervals[i][1])]
                    temp = output[j]
                    output.pop()
                    j-=1
            else:
                output.append(intervals[i])
        return output
            