class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        for i in range(1,len(words)):
            if d[words[i-1][0]] > d[words[i][0]]:
                return False
            elif d[words[i-1][0]] == d[words[i][0]]:
                for j in range(1,len(words[i-1])):
                    if j>= len(words[i]) or d[words[i-1][j]] > d[words[i][j]]:
                        return False
                    elif d[words[i-1][j]] < d[words[i][j]]:
                        break
        return True
                    
            
