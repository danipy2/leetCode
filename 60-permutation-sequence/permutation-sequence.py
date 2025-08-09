class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr1 = [str(i) for i in range(1,n+1)]
        self.count = 0
        self.ans = 0
        def permu(s,st):
            if self.ans:
                return 
            if len(st) == len(arr1):
                self.count +=1
                if self.count == k:
                    self.ans = "".join(st)
                return 
            for i in arr1:
                if i not in s:
                    st.append(i)
                    s.add(i)
                    permu(s,st)
                    st.pop()
                    s.remove(i)
        permu(set(),[])
        return self.ans

