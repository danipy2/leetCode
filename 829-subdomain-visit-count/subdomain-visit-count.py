class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        mydict = defaultdict(int)
        for domain in cpdomains:
            value,cpdom = domain.split()
            scp = cpdom.split(".") 
            for i in range(len(scp)):
                js = ".".join(scp[i:])
                mydict[js] += int(value)
        return [str(value)+" " + key for key,value in mydict.items()]
            

        