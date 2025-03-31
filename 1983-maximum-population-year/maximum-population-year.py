class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0 for i in range(102)]
        for i in logs:
            startindex = i[0]-1950
            lastindex = i[1]-1950
            arr[startindex] += 1
            arr[lastindex] -= 1
        total = 0 
        maxm = [0,0]
        for i in range(len(arr)):
            total += arr[i]
            if total > maxm[0]:
                maxm = [total,i]
        return 1950+maxm[1]