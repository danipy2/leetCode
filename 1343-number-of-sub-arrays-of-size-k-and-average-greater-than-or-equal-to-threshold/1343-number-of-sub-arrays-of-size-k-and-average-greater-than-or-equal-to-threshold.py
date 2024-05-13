class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total= 0
        if len(arr)>=k:
            ave = sum(arr[0:k])/k
            if ave >=threshold:
                total +=1
            for i in range(k,len(arr)):
                ave = ave - (arr[i-k]/k)+(arr[i]/k)
                if ave >= threshold:
                    total +=1
        return total
                    


        