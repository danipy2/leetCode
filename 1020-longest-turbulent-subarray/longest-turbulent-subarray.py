class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        maxm = 1
        sign = 0
        for i in range(len(arr)-1):
            if (sign==1 and arr[i] > arr[i+1]) or( sign== -1 and arr[i] < arr[i+1]) or (arr[i]==arr[i+1]):
                maxm = max(i-l+1,maxm)
                sign =0
                l = i
            elif i==len(arr)-2:
                maxm = max(i-l+2,maxm)
            if sign == 0:
                if arr[i] >arr[i+1]:
                    sign = 1
                elif arr[i] < arr[i+1]:
                    sign = -1
                else:
                    l+=1
            else:
                sign*=-1
        
        return maxm