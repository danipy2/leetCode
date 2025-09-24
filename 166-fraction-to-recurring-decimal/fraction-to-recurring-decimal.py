class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pn,pv = numerator,denominator
        numerator,denominator = abs(numerator),abs(denominator)
        n,m = numerator,denominator
        if n%m==0:
            if pn * pv< 0:
                return "-"+str(n//m)
            return str(n//m)
        s = {}
        div =1
        ans = []
        while n<m:
            n*=10
            ans.append("0")
            if -1 not in s:
                    s[-1] = 0
                    ans.append(".")
        
        def zdev(n):
            nonlocal ans
            if n in s:
                ind = s[n]
                ans = ans[:ind] + ["("] + ans[ind:] +[")"]
                return
            else:
                s[n] = len(ans)
                
            if n<denominator:
                if -1 not in s:
                    s[-1] = 0
                    ans.append(".")
                    s[n] = len(ans)
                n*=10
                while n<denominator:
                    ans.append("0")
                    n*=10
            rem = n%denominator
            res = n//denominator
            ans.append(str(res))
            if rem==0:
                return 
            zdev(rem)
        zdev(n)
        if pn * pv< 0:
            return "-"+"".join(ans)
        return "".join(ans)
            

