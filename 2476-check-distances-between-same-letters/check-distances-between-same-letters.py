class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        myset = set()
        for i in range(len(s)):
            if s[i] not in myset:
                index = distance[ord(s[i])-97] +i+1
                if  index >=len(s) or s[index] != s[i]:
                    return False
                myset.add(s[i])
        return True