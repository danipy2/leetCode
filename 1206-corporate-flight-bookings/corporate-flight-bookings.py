class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0 for i in range(n+2)]
        for i in range(len(bookings)):
            l,r,seat = bookings[i]
            arr[l-1] += seat
            arr[r] -= seat
        ans = []
        total = 0
        for i in range(n):
            total += arr[i]
            arr[i] = total
            ans.append(arr[i])
        return ans
