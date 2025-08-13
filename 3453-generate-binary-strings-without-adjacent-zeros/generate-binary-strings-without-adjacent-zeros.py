class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def validSubs(arr):
            if len(arr) == n:
                ans.append("".join(arr))
                return 
            if arr[-1] == "0":
                arr.append("1")
                validSubs(arr)
                arr.pop()
            else:
                arr.append("1")
                validSubs(arr)
                arr[-1]="0"
                validSubs(arr)
                arr.pop()
        validSubs(["0"])
        validSubs(["1"])
        return ans


