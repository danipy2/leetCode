class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        myd = {}
        count = 0
        for i in answers:
            if i==0 or i  not in  myd or myd[i]==0:
                myd[i] = i
                count+= i+1                           
            else:
                myd[i]-=1
                
                
        return count
               