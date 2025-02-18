class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []     
        st = ""
        l = len(num)-k
        for i in range(len(num)):
            while stack and k>0 and stack[-1] > num[i]:
                k-=1
                stack.pop()
            else:
                stack.append(num[i])
        while len(stack) >l:
            stack.pop()
        st = "".join(stack)
        st = st.lstrip('0')
        if st=="":
            return "0"
        return st