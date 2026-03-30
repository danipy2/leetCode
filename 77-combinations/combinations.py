class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def do(arr,num):
            if num>n or len(arr)==k:
                if len(arr)==k:
                    ans.append(arr.copy())
                return
            arr.append(num)
            do(arr,num+1)
            arr.pop()
            do(arr,num+1)
        do([],1)
        return ans