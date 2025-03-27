class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0 for i in range(n+2)]
        for i in range(len(bookings)):
            l,r,seat = bookings[i]
            arr[l] += seat
            arr[r+1] -= seat
        ans = []
        for i in range(1,n+1):
            arr[i] += arr[i-1]
            ans.append(arr[i])
        return ans
