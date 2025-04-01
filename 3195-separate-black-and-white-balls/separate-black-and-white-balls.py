class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        total = 0
        for i in range(len(s)):         
            if s[i] == "0":
                count += total
            else:
                total+=1
            
        return count
