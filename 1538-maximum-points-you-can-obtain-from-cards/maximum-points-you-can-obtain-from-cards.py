class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = 1
        j = len(cardPoints)-2
        arr1 = [cardPoints[0]]
        arr2 = [cardPoints[-1]]
        while(i<len(cardPoints)):
            arr1.append(cardPoints[i]+arr1[-1])
            arr2.append(cardPoints[j]+arr2[-1])
            i+=1
            j-=1
        arr3 = []
        for i in range(len(arr1)-1,-1,-1):
            arr3.append(arr1[i])
        arr3.append(0)
        arr3 += arr2
        maxm = 0
        
        l = 0 
        if len(arr1)>k:
            l = len(arr1)-k
        r = (l+k)
        while(r<len(arr3) and  l<=len(arr1)):
            x = 0
            if (l<len(arr1) and r<len(arr1)) or (l>len(arr1) and r>len(arr1)  ):
                x = abs(arr3[l] -arr3[r])
            else:
                x = arr3[l] +arr3[r]
            if x >maxm:
                maxm = x
            l+=1
            r+=1
        return maxm
        