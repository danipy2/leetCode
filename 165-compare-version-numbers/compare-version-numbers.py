class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        maxm = max(len(v1),len(v2))
        print(v1,v2)
        for i in range(maxm):
            a1 = (v1[i].lstrip("0")) if i<len(v1) else 0
            a2 = (v2[i].lstrip("0")) if i<len(v2) else 0
            a1 = int(a1) if a1 else 0
            a2 = int(a2) if a2 else 0
            if a1==a2:
                continue
            if a1>a2:
                return 1
            else:
                return -1
        return 0