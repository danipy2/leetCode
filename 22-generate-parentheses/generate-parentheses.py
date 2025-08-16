class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gen(arr,stack):
            if len(arr)== n*2:
                if not stack:
                    ans.append("".join(arr))
                return 
            arr.append("(")
            stack.append("(")
            gen(arr,stack.copy())
            arr.pop()
            stack.pop()
            if stack:
                arr.append(")")
                stack.pop()
                gen(arr,stack.copy())
                arr.pop()

        gen([],[])

        return ans