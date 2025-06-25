class Solution:
    def myAtoi(self, s: str) -> int:
        self.arr  = []
        mod  = 2**31 
        
        s = s.lstrip()
        if len(s) ==0:
            return 0
        numb = 0
        if s[0] == "+" or s[0] == "-":
            self.change(s,1)
        else:
            self.change(s,0)
        c = len(self.arr)-1
        for i in self.arr:
            numb += i*(10**c)
            c-=1
        if s[0] == "-":
            if numb > mod:
                return -1 * (mod)
            return -1 * numb
        if numb >= mod:
            return mod - 1

        return numb
    def change(self,s,i):
        if i >=len(s):
            return 
        char = s[i]
        if self.arr:
            if not char.isdigit():
                return 
            self.arr.append(int(char))
            self.change(s,i+1)
        else:
            if char == "0":
                return self.change(s,i+1)
            if char.isdigit():
                self.arr.append(int(char))
                self.change(s,i+1)

        

