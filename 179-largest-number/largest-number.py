class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = list(map(str,nums))
        def compare(a,b):
            if a+b < b +a:
                return 1
            elif a+b != b+a:
                return -1
            else:
                return 0
        n.sort(key=cmp_to_key(compare))
        if n[0] == "0":
            return "0"
        return "".join(n)