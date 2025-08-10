class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(possible,str1,str2,st):
            for i in range(0,len(str1),r+1):
                w = str1[i:i+r+1]
                if w != possible:
                    return ""
            for i in range(0,len(str2),r+1):
                w = str2[i:i+r+1] 
                if w!=possible:
                    return ""
            return possible
        st = str1
        if len(str1) > len(str2):
            st = str2
        lgth = len(set(st))
        r = 0
        count = 0
        s = set()
        ans = ""
        for i in st:
            if i not in s:
                s.add(i)
                count+=1
                if count > lgth:
                    return ans
            if count ==lgth:
                x = gcd(st[:r+1],str1,str2,st)
                if x:
                    ans =  x
            
            r+=1
        
        return ans