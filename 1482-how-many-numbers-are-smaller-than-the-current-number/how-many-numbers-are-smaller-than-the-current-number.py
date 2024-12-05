class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        mydict = {}
        temp = -1
        count = 1
        for i in arr:
            if i in mydict:
                count+=1
            else:
                if temp!=-1:
                    mydict[i] = mydict[temp]+count
                else:
                    mydict[i] = 0
                temp = i
                count = 1
        ans = []
        for i in nums:
            ans.append(mydict[i])
        return ans   
                