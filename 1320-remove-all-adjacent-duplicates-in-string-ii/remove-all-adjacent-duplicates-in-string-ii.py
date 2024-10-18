class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [s[0]]
        count = 1
        for i in s[1:]:
            if len(stack)-count>=0 and stack[len(stack)-count] == i:
                while len(stack)-count>=0 and stack[len(stack)-count] == i: 
                    count+=1
                if count ==k:
                    stack = stack[:(len(stack)-k)+1]
                    count = 1
                    continue
                    
            else:
                count = 1
            stack.append(i)
        return "".join(stack)
            