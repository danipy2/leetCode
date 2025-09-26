class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,0,-1):
            if arr[i]<arr[i-1]:
                ind = i
                for j in range(i+1,len(arr)):
                    if arr[j]<arr[i-1]:
                        if arr[ind]!= arr[j]:
                            ind = j
                arr[ind],arr[i-1]=arr[i-1],arr[ind]
                break
            
        return arr