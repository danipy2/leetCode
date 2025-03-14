class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 0
        count = 0
        i=0
        ratings.append(ratings[-1])
        cond = True
        maxm = 0
        while i<len(ratings)-1:
            while i<len(ratings)-1 and ratings[i] > ratings[i+1]:             
                if cond or count:
                    total+= 1+count
                    count+=1
                i+=1
                if count==maxm:
                    count+=1
                    total+=1
                print(1,total)
                cond = True
            count = 0
            maxm = 0
            while i<len(ratings)-1 and ratings[i] < ratings[i+1]:
                total+= 1+count
                count+=1
                i+=1
                cond = False
                maxm +=1
                print(11111111,total)
            while i<len(ratings)-1 and  ratings[i] == ratings[i+1]:
                cond = True
                i+=1
                maxm = 0
            print(total,i)
            
            count=0
        return len(ratings)+total-1
            
            

