class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def findpart(parts,arr):
            if not arr:
                ans.append(parts.copy())
                return 
            for i in range(len(arr)):
                word = arr[0:i+1]
                if word == word[::-1]:
                    parts.append(arr[0:i+1])
                    findpart(parts,arr[i+1:])
                    parts.pop()
        findpart([],s)
        return ans
            
