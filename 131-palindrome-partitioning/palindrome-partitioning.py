class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        palindrome = set()
        def findpart(parts,arr):
            if not arr:
                ans.append(parts.copy())
                return 
            for i in range(len(arr)):
                word = arr[0:i+1]
                if word in palindrome or word == word[::-1]:
                    palindrome.add(word)
                    parts.append(arr[0:i+1])
                    findpart(parts,arr[i+1:])
                    parts.pop()
        findpart([],s)
        return ans
            
