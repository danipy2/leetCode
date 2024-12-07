class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = 1
        r = k
        count = 0
        total = 0
        for i in range(1,k-1):
            if colors[i]==colors[i-1] or colors[i]==colors[i+1]:
                count+=1
        if count == 0:
            total +=1
        while(l<len(colors)):
            if (colors[l] == colors[l-1] or colors[(l+1)%len(colors)] == colors[l]):
                count -= 1
            if colors[(r-1)%len(colors)] == colors[(r-2)%len(colors)] or colors[(r)%len(colors)] == colors[(r-1)%len(colors)]:
                count+=1
            if count ==0:
                total+=1
            l+=1
            r+=1
        return total