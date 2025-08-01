class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr1 = []
        
        def find(a,ans):
            if not a:
                arr1.append(ans)

                return 
            for ind ,val in enumerate(a):
                ans.append(val)
                find(a[:ind]+a[ind+1:],ans.copy())
                ans.pop()
        find(nums,[])
        return arr1

