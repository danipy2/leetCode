class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        second = len(s)-1
        for i in range(ceil(len(s)/2)):
            temp = s[first]
            s[first] = s[second]
            s[second] = temp
            first +=1
            second -= 1

        