class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total = 0
        for i, j in zip(seats,students):
            total +=  i-j if i >=j else j- i
        return total