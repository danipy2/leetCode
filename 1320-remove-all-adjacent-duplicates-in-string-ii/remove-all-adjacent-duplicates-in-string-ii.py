class Solution:
        def removeDuplicates(self, s, k):
            stack = [['A', 0]]
            for i in s:
                if stack[-1][0] ==i:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([i, 1])
            return ''.join(i * k for i, k in stack)
                