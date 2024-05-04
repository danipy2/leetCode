class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        places = []
        left = 0
        arr = []
        for i in range(len(s)):
            if s[i] == c:
                places.append(i)
        for i in range(len(s)):
                if i >places[left] and left+1 <len(places):
                    left += 1
                if left>=len(places):
                    break
                else:
                    arr.append(min(abs(i-places[left-1]),abs(i-places[left])))
        return arr
