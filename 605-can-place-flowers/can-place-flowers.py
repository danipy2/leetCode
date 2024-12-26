class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if (flowerbed[i]==0 )and (i==0 or flowerbed[i-1]==0 )and (flowerbed[i]==0) and ((i+1>=len(flowerbed))or flowerbed[i+1]==0):
                count+=1
                flowerbed[i] = 1

        return count>=n