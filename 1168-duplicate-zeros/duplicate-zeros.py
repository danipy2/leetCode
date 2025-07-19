class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        c  = arr.copy()
        l = 0
        ind = -1
        for i in range(len(arr)):
            arr[i] = c[l]
            
            if c[l]==0 and ind!=l:
                l-=1
                ind = l+1
            l+=1
            
        