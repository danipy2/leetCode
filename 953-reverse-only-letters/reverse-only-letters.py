class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s)-1
        arr = list(s)
        print(arr)
        while i <j:
            while i < j and (not s[i].isalpha()):
                
                i+=1
            while j>i and (not s[j].isalpha()):
                j-=1
                
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        return "".join(arr)

