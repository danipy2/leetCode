class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while (left <= right):
            mid = (left + right) // 2
            if (((mid) * (mid + 1)) / 2)<=n and ((mid + 2) * (mid + 1) / 2)>n:
                print(mid,3)
                return mid
            if ((mid + 1) * mid) / 2 <= n:
                left = mid + 1
            else:
                right = mid - 1
        return mid