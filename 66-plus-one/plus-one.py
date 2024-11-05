class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        st = "".join(s)
        st1 = str(int(st)+1)
        s = [int(i) for i in st1]
        return s