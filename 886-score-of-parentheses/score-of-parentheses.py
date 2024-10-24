class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        contain = ""
        ss = ""
        output = 0
        for i in s:
            if i=="(":
                ss+="+("
            else:
                if contain and contain=="(":
                    ss+="1)"
                else:
                    ss+=")*2"
            contain = i
        return eval(ss)

                