class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        output = []
        cond = False
        for i in range(len(s)):
            if s[i]!=c:
                if len(output)==0:
                    output.append(0)
                else:
                    output.append(output[-1]+1)
            else:
                left = i-1
                output.append(0)
                while left>=0 and ((output[left]> (i-left))or cond==False ):
                    output[left] = i-left
                    left-=1
                cond = True

            
        return output