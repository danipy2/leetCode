class Solution:
    def reorganizeString(self, s: str) -> str:
        arr = [0] * 26
        indx = ord('a')
        for i in s:
            arr[ord(i)-indx]+=1
        heap = []
        for i in range(26):
            if arr[i]:
                heapq.heappush(heap,(arr[i],chr(indx+i)))
        ans = []
        while heap:
            rep , let = heapq.heappop(heap)
            temp = []
            while rep and ans:
                temp.append(let)
                temp.append(ans.pop())
                rep-=1
            temp.extend(ans[::-1])
            if rep:
                temp.extend([let]*rep)
            ans = temp[:]
        for i in range(1,len(ans)):
            if ans[i] == ans[i-1]:
                return ""

        return "".join(ans)
        



                
        