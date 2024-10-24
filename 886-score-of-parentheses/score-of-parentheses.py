class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ss = ""
        output = 0
        for i in s:
            if i=="(":
                stack.append(i)
                ss+="+("
            else:
                if stack and stack[-1]=="(":
                    ss+="1)"
                    stack.append(i)
                else:
                    ss+=")*2"
                    stack.append(i)
        return eval(ss)

                