class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left =0
        dic = {}
        dic2 = {}
        dic1 = {}
        for i in t:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                dic2[i] = False
        count = 0
        max1 = len(s)+1
        min_str = ""
        for i in range(len(s)):
            if s[i] in dic:
                if s[i] not in dic1:
                    if dic[s[i]]==1:
                        if dic2[s[i]] == False:
                            count +=1
                            dic2[s[i]] = True
                    dic1[s[i]] = 1
                else:
                    if (dic[s[i]]- dic1[s[i]]==1):
                        if dic2[s[i]]== False:
                            count +=1
                            dic2[s[i]] = True
                    dic1[s[i]] +=1
            if count == len(dic):
                while count == len(dic):
                    if s[left] in dic:
                        dic1[s[left]] -=1
                        if dic1[s[left]] < dic[s[left]]:
                            count -=1
                            dic2[s[left]] = False
                            if max1 > ((i - left)+1):
                                max1 = ((i - left)+1)
                                min_str = s[left:i+1]
                    left +=1
        return min_str


        