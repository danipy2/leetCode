class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        stack2 = []
        count = 0
        for i in range(len(s)):
            if s[i] ==")":
                if stack:
                    stack.pop()
                    stack2.append(s[i])
                else:
                    count+=1
            elif s[i]=="(":
                stack.append([s[i],i-count])
                stack2.append(s[i])
            else:
                stack2.append(s[i])
        for i in stack:
            stack2[i[-1]] = "*"
        st = ""
        for i in stack2:
            if i !="*":
                st+=(i)
        return st

            



