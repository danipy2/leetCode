class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p = [0 for i in s]
        p[0] = shifts[0]
        s1 = [i for i in s]
        for i in range(1,len(shifts)):
            p[i] = shifts[i] + p[i-1]
        s1[0] = chr(ord('a')+((ord(s1[0])+p[-1])-97)%26)
        for i in range(len(shifts)-1):
            s1[i+1] = chr(ord('a')+((ord(s1[i+1])+p[-1]-p[i])-97)%26)
        return "".join(s1)


