class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mydic = {}
        for i in nums:
            if i in mydic:
                mydic[i] += 1
            else:
                mydic[i] = 1
        maxm = 0
        count = 1
        for i in nums:
            count = 1
            if i-1 not in mydic:
                while(i+1 in mydic):
                    count+=1
                    i+=1
                if count > maxm:
                    maxm = count
        return maxm
                
