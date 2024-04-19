class Solution:
    def fairCandySwap(self,aliceSizes,bobSizes):
        left = 0
        right = 0 
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        aliceSizes.sort()
        bobSizes.sort()
        while(left<len(aliceSizes) and right<len(bobSizes) ):
                if (sum2-bobSizes[right]+aliceSizes[left] )  ==  (sum1+bobSizes[right]-aliceSizes[left] ):
                    return [aliceSizes[left],bobSizes[right]]
                elif (sum2-bobSizes[right]+aliceSizes[left] )  > (sum1+bobSizes[right]-aliceSizes[left] ):
                    right += 1
                else:
                    left += 1