class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [s[0]]
        stack2 = [1]
        for i in s[1:]:
            if stack and (len(stack)-(stack2[-1]))>=0 and stack[(len(stack)-(stack2[-1]))] == i:
                if stack2[-1]+1 == k:
                    stack = stack[:(len(stack)-k)+1]
                    stack2.pop()
                    continue
                stack2[-1] +=1
                    
            else:
                stack2.append(1)
            stack.append(i)
        return "".join(stack)
            