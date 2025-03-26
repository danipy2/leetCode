class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i =='a':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i=='b':
                    stack.append(i)
                else:
                    if stack[-1]=='b':
                        stack.pop()
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True