class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def find1(a,used):
            if len(used) == len(nums):
                arr.append(a.copy())
                return 
            for ind ,val in enumerate(nums):
                if val not in used:
                    used.add(val)
                    a.append(val)
                    find1(a,used)
                    a.remove(val)
                    used.remove(val)
                
        find1([],set())
        return arr

