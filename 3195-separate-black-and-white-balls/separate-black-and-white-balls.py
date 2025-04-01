class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        l = 0
        total = 0
        for i in range(len(s)):  
            total += int(s[i])         
            if s[i] == "0":
                count += total
            
        return count
