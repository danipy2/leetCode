class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        total = 0
        s = 0 
        while l <r:
            lv = skill[l]
            rv = skill[r]
            ns = lv + rv
            if s ==0:
                s = ns
            elif s != ns:
                return -1
            total+= lv * rv
            l+=1
            r-=1
        return total