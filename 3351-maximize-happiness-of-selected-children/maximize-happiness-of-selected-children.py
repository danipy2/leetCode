class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        if k>=1:
            happiness.sort(reverse=True)
        i = 0
        while k-i and i <len(happiness):
            if happiness[i] -i >0:
                total += happiness[i] -i
            else:
                break
            i+=1
        return total
        
        return total
