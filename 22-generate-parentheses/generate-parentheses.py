class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gen(arr,stack):
            if len(arr)== n*2:
                if not stack:
                    ans.append("".join(arr))
                return 
            arr.append("(")
            stack+=1
            gen(arr,stack)
            arr.pop()
            stack-=1
            if stack:
                arr.append(")")
                stack-=1
                gen(arr,stack)
                arr.pop()

        gen([],0)

        return ans