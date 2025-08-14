class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern = pattern+"I"
        arr = []
        minm = 1
        stack = []
        indx = 0
        while indx < len(pattern):
            while indx < len(pattern) and pattern[indx]!="I":
                stack.append(1)
                indx+=1
            if indx < len(pattern):
                stack.append(len(arr)+1)
                for i in range(len(stack)-2,-1,-1):
                    stack[i] = stack[i+1]+1
                arr.extend(stack)
                stack = []
            indx+=1

        return "".join([str(i) for i in arr])
            

        
                
