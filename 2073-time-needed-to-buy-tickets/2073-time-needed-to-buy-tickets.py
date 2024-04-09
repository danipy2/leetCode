class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        while(tickets[k]):
            if tickets[i%len(tickets)]:
                count += 1
                tickets[i%len(tickets)] -= 1
            i+=1
        return count
            

        