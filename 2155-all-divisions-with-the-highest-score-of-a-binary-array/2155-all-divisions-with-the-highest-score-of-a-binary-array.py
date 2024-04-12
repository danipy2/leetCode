class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count = 0
        max_ = [0]
        first = 0
        ones = 0
        for i in nums:
            if i:
                ones +=1

        zeros = 0
        arr =[ones]
        max1 = ones
        for i in range(len(nums)):
            if nums[first]==0:
                zeros +=1
            else:
                ones-=1
            count = zeros + ones
            if max1 < count:
                max1 = count
                max_ = [i+1]
            elif max1 == count:
                max_.append(i+1)
            arr.append(count)
            count = 0
            first +=1

        return max_


            