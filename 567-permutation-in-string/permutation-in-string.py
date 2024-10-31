class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        myset = set()
        if len(s1)>len(s2):
            return False
        for i in s1:
            if i in myset:
                dic[i] +=1 
            else:
                myset.add(i)
                dic[i] = 1
        count=0
        for i in range(len(s1)):
            if s2[i] in myset:
                dic[s2[i]] -=1
                if dic[s2[i]]==0:
                    count+=1
        if len(myset)==count:
            return True
        left = 0
        right=len(s1)-1

        while(right+1<len(s2)):
            right+=1
            if s2[right] in myset:
                dic[s2[right]] -=1
                if dic[s2[right]]==0:
                    count +=1
            if s2[left] in myset:
                if dic[s2[left]]==0:
                    count-=1
                dic[s2[left]] +=1
            if count == len(myset):
                return True
            left+=1
        return False
