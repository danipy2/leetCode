class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        mdict = defaultdict(int)
        for domains in cpdomains:
            arr = domains.split()
            d = arr[1].split(".")
            for i in range(len(d)):
                mdict[".".join(d[i:])]+=int(arr[0])
                print(mdict)
        
        return [str(value)+" "+key for key,value in mdict.items()]
