class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mset = set()
        arr = [0] *n
        new = [0] *n
        for l,r in trust:
            arr[l-1]+=1
            new[r-1] += 1
        for i in range(len(new)):
            if new[i] == n-1 and arr[i] == 0 :
                return i+1
        return -1
