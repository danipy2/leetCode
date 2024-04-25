class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        while(left<=right):
           mid = (left+right)//2
           if citations[mid] == len(citations)-mid:

                return citations[mid] 
           if (citations[mid] > (len(citations)-mid ))and(mid==0 or citations[mid-1] <=(len(citations)-mid)):
                print(2,citations[mid] > (len(citations)-mid))
                return  len(citations)-mid
           elif citations[mid] > (len(citations)-mid ):
                right = mid -1
            
           else:
                left = mid +1
        return 0