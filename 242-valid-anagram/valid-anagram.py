class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dic1 = Counter(s)
        dic2 = Counter(t)

        if dic1!=dic2:
            return False
        for key in dic1:
            if dic1[key] != dic2[key]:
                return False
        return True