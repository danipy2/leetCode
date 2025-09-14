class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        v = set([i for i in wordlist])
        wv = {}
        wvv = {}
        visted = {}
        ans = []
        vo = set(["a","e","i","u","o"])
        s1 = {}
        def fun(w):
            arr = []
            arr1 = []
            for j in range(len(w)):
                if w[j] in vo:
                    arr1.append(str(j))
                else:
                    arr.append(w[j])
            st = "".join(arr)
            st1 = "".join(arr1)
            return [st,st1]
        for i in wordlist:
            w = i.lower()
            if w not in  s1:
                s1[w] = i
            st,st1 = fun(w)
            tot = st+st1
            if tot not in wvv:
                wvv[tot] = i
        for i in queries:
            if i in v:
                ans.append(i)
                continue
            ii = i.lower()
            if ii in s1:
                ans.append(s1[ii])
                continue
            if ii in visted:
                ans.append(visted[ii])
                continue
            word = ""
            st,st1 = fun(i.lower())
            tot = st+st1
            if tot in wvv:
                word = wvv[tot]
            ans.append(word)
        return ans
        
                
                        
                
