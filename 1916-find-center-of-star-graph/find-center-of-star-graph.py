class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        arr = [0] * (len(edges)+2)
        maxm = -1
        ind = -1
        for i,j in edges[:3]:
            arr[i] +=1
            arr[j] +=1
            if arr[i]>maxm:
                ind = i
                maxm = arr[i]
            if arr[j] > maxm:
                ind = j
                mam = arr[j]
        return ind
            
        