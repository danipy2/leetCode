class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = ""
        for i in s:
            st+= str(ord(i)-ord('a')+1)

        total =sum(int(i) for i in st)
        while k>1:
            k-=1
            total = sum(int(i) for i in str(total))
        return total