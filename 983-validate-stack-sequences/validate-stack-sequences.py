class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l = 0
        for i in popped:
            if stack and(stack[-1]==i):
                stack.pop()
            else:
                while l<len(pushed) and i != pushed[l]:
                    stack.append(pushed[l])
                    l+=1
                l+=1
        return len(stack)==0