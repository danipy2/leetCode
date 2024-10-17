class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                first = stack.pop()
                second = stack.pop()
                result = first + second
                stack.append(result)
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                result = second-first
                stack.append(result)
            elif i == "*":
                first = stack.pop()
                second = stack.pop()
                result = second*first
                stack.append(result)
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                result = int(second/first)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()

                
                
