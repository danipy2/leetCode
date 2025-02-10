class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        p1 = [nums[0]]
        p2 = [nums[-1]]
        minm = 10**5 +1
        for i in range(1,len(nums)): 
            p1.append(p1[i-1]+nums[i])
            p2.append(p2[i-1]+nums[(i*-1)-1])
        print(p1,p2)
        index = 0
        for i in range(len(p1)):
            rave = p1[i]//(i+1)
            lave = 0
            if i!=len(p1)-1:
                lave=(p2[len(p2)-i-2])//(len(nums)-i-1)
            x = abs(rave-lave)
            if x < minm:
                minm = x
                index = i
        return index
