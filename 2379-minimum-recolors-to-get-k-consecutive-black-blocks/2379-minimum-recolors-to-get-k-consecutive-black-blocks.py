class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count+=1
        minim = count
        for i in range(k,len(blocks)):
            if blocks[i-k] == "W" and blocks[i] == "B":
                count -= 1
            elif blocks[i-k] == "B" and blocks[i] == "W":
                count +=1
            if count < minim:
                minim = count
        return minim
                