class Solution:
    def equalFrequency(self, word: str) -> bool:
        s = {}
        for i in word: 
            if i in s: 
                s[i] += 1
            else:
                s[i] = 1
        t = 0
        v = -1
        if len(s)==1:
            return True
        for key in s:
            if s[key] == v:
                t+=1
            else:
                if t:
                    t-=1
                else:
                    t=1
                    v=s[key]
        count = 0
        if len(s) == 2:
            for key in s:
                if s[key]!=v:
                    count+=1
                    if s[key]!=1 and v!=1 and abs(s[key]-v)!=1:
                        return False
                if count ==1 or (count==0 and v==1):
                    return True

        for key in s:
            if s[key] != v:
                if (v+1 ==s[key] or s[key]==1) and count ==0:
                    count +=1
                else:
                    return False
        if count ==1 or (count==0 and v==1):
            return True
        
        return False
                
        

            
                        