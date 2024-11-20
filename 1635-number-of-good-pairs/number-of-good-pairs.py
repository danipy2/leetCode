class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_arr = [0 for i in range(0,100)]
        mydic = {}
        myset = set()
        for i in nums:
            if i in myset:
                if count_arr[i-1] == 0 :
                    mydic[i] = 1
                else:
                    mydic[i] += 1
                count_arr[i-1] += mydic[i]
            
            myset.add(i)
        return sum(count_arr)
        