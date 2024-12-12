class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0]
        for i in customers:
            x = 0
            if i == "Y":
                x+=1
            prefix.append(prefix[-1]+x)
        minm = len(prefix)+1
        index = 0
        for i in range(len(prefix)):
            temp = (prefix[-1] -prefix[i])
            if i:
                temp += i-prefix[i] 
            if temp<minm:
                minm = temp
                index = i
        return index
