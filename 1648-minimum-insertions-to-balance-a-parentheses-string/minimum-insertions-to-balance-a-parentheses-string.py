class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        i = 0
        for i in s:
            if i=="(":
                if len(stack)>=1 and stack[-1]==")":
                    stack.pop()
                    stack.pop()
                    stack.append(i)
                    count+=1

                else:
                    stack.append(i)
            else:
                if len(stack)==0:
                    stack.append("(")
                    stack.append(i)
                    count+=1
                else:
                    if stack[-1]=="(":
                        stack.append(i)
                    else:
                        stack.pop()
                        stack.pop()
        while stack:
                if stack[-1]==")":
                    stack.pop()
                    stack.pop()
                    count+=1
                else:
                    stack.pop()
                    count+=2
        return count
             