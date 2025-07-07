class NumArray:
    def __init__(self, nums: List[int]):
        self.n = nums
        self.nums = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            index = i+1
            while index <= len(self.nums):
                self.nums[index-1] += nums[i]
                x = index & -index
                index =index +x 
    def update(self, index: int, val: int) -> None:
        diff = val - self.n[index]
        self.n[index] = val
        index += 1
        while index <= len(self.nums):
            self.nums[index-1] += diff
            x = index & -index
            index =index +x 


    def sumRange(self, left: int, right: int) -> int:
        r = 0
        l = 0
        right +=1
        while right >0:
            r+= self.nums[right-1] 
            right = right - (right & -right)
        while left >0:
            l += self.nums[left-1]
            left = left - (left & -left)
        return r-l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)