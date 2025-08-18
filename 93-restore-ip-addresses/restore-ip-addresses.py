class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        stack = []
        def dfs(ind,c):
            if c==4:
                print(stack)
                if ind>=len(s):
                    stack.pop()
                    ans.append("".join(stack))
                    stack.append(".")
                return
            n = 0
            while ind<len(s):
                n *= 10 
                n+= int(s[ind])
                if  0<=n<=255:
                    stack.append(str(n))
                    stack.append(".")
                    dfs(ind+1,c+1)
                    stack.pop()
                    stack.pop()
                else:
                    break
                if n==0:
                    break
                ind+=1
               
                
                
        dfs(0,0)
        return ans
