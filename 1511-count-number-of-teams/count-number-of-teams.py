class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cache = {}
        def back(i,asc,count):
            res = 0
            if (i,asc,count) in cache:
                return cache[(i,asc,count)]
            if count == 3:
                return 1
            if i == len(rating):
                return 0
            for j in range(i+1,len(rating)):
                if asc and rating[j] < rating[i]:
                    res += back(j,asc,count+1)
                elif not asc and rating[j] > rating[i]:
                    res += back(j,asc,count+1)
            cache[(i,asc,count)] = res
            return res
        res = 0
        for i in range(len(rating)):
            res +=back(i,True,1)
            res +=back(i,False,1)
        return res