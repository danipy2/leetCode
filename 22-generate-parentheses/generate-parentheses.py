class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gen(arr,op,cl):
            if len(arr)== n*2:
                ans.append("".join(arr))
                return 
            if op < n:
                arr.append("(")
                gen(arr,op+1,cl)
                arr.pop()
            if op>cl:
                arr.append(")")
                gen(arr,op,cl+1)
                arr.pop()

        gen([],0,0)

        return ans