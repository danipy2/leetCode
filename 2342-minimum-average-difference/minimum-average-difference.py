class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0           # Initialize left sum
        min_diff = float('inf')  # Initialize minimum difference to infinity
        min_index = -1         # Initialize minimum index

        for i in range(n):
            left_sum += nums[i]  # Update left sum with the current element
            
            # Calculate left average
            left_avg = left_sum // (i + 1)
            
            # Calculate right average
            if i < n - 1:
                right_avg = (total_sum - left_sum) // (n - i - 1)
            else:
                right_avg = 0  # If it's the last element, right average is 0
            
            # Calculate absolute difference
            diff = abs(left_avg - right_avg)

            # Update minimum difference and index if a new minimum is found
            if diff < min_diff:
                min_diff = diff
                min_index = i

        return min_index

