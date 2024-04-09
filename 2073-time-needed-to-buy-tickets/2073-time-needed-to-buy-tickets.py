class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sum = 0
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] <=tickets[k]:
                    sum+=tickets[i]
                else:
                    sum+=tickets[k]
            else:
                if tickets[i] <tickets[k]:
                    sum+=tickets[i]
                else:
                    sum+=tickets[k]-1
        return sum
            

        