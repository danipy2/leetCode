class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        places = []
        left = 0
        arr = []
        for i in range(len(s)):
            if s[i] == c:
                places.append(i)
        for i in range(len(s)):
                if s[i] == c:
                    arr.append(0)
                    left += 1
                elif i<places[0]:
                    arr.append(places[0]-i)
                elif i>places[-1]:
                    arr.append(i-places[-1])
                else:
                    arr.append(min(i-places[left-1],places[left]-i))
        return arr
