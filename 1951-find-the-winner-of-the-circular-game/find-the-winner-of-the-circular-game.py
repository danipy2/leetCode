class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        for i in range(1,n+1):
            index = (index+k) % i
            
        return index+1

