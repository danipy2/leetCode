class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        count = complexity.count(complexity[0])
        if count >1 or complexity[0]>min(complexity):
            return 0
        mod = 1000000007
        def fact(n,mod):
            if n <=1:
                return 1
            return (fact(n-1,mod)*n)%mod
        return fact(len(complexity)-1,mod)