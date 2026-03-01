class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count1 =0
        count2 = 0
        for i in range(1,len(colors)-1):
            l = "A"
            k = "B"
            if colors[i]==k and colors[i-1]==k and colors[i+1]==k:
                count2+=1
            elif colors[i]==l and colors[i-1]==l and colors[i+1]==l:
                count1+=1
        return count1>count2