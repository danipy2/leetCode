class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen={0:1}
        count=0
        total=0
        for num in nums:
            total+=num
            remainder=total-goal
            if remainder in seen:
                count+=seen.get(remainder,0)
            seen[total]=seen.get(total,0)+1
        return count
