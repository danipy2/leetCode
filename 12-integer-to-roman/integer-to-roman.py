class Solution:
    def intToRoman(self, num: int) -> str:
        Dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        st = str(num)
        length = len(st)
        s = ""
        for j in st:
            i = int(j)
            if i!=4 and i!=9:
                length -=1
                if i<5:
                    s+= Dict[10**length]*i
                else:
                    s+= Dict[10**length*5]
                    s+= Dict[10**length]*(i-5)
            else:
                length-=1
                s+= Dict[10**length]
                s+= Dict[10**length* (i+1)]
        return s