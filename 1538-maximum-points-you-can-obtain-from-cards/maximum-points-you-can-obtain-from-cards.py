class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if 2*k < len(cardPoints):
            cardPoints = cardPoints[:k] + cardPoints[-k:] 



        min_sum_len = len(cardPoints) - k
        total_sum = sum(cardPoints)

        if min_sum_len == 0:
            return total_sum
        
        min_sum = total_sum
        current_sum = sum(cardPoints[0:min_sum_len])
        min_sum = min_sum if min_sum < current_sum else current_sum
        to_sub = cardPoints[0]

        for i in range(min_sum_len, len(cardPoints)):
            current_sum = current_sum - to_sub + cardPoints[i]  
            min_sum = min_sum if min_sum < current_sum else current_sum
            to_sub = cardPoints[i - min_sum_len + 1]
        
        return total_sum - min_sum