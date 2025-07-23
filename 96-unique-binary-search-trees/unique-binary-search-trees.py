class Solution:
    def numTrees(self, n: int) -> int:
        def numTrees(n):
            if n <= 1:
                return 1
            total = 0

            for root in range(1, n //2 +1):
                left = numTrees(root - 1)
                right = numTrees(n - root)
                total += left * right
            total *= 2
            if n%2:
                root = (n+1)//2
                left = numTrees(root - 1)
                right = numTrees(n - root)
                total += left * right
                
            return total
        return numTrees(n)
