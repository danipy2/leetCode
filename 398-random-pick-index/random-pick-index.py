class Solution:

    def __init__(self, nums: List[int]):
        self.s = {}
        for i in range(len(nums)):
            if nums[i] in self.s:
                self.s[nums[i]].append(i)
            else:
                self.s[nums[i]] = [i]

    def pick(self, target: int) -> int:
        return random.choice(self.s[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)