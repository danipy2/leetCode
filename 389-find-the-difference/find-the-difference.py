class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = [0] * 26
        arr1 = [0] * 26
        sind = ord('a')
        for i in s:
            arr[ord(i)-sind] += 1
        for i in t:
            arr1[ord(i)-sind] += 1
        for i in range(26):
            if arr1[i] >arr[i]:
                return chr(sind+i)