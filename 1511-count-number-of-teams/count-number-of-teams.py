class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def query(n,ar):
            l = n-1
            r = len(arr)-1
            t1 = 0
            t2 = 0
            t = 0
            while l >0:
                t1 += ar[l]
                l -= l&-l
            while n >0:
                t += ar[n]
                n -= n&-n
            while r >0:
                t2 += ar[r]
                r -= r & -r
            return [t1 ,t2-t]
        def update(val,op,ar):
            while val < len(ar):
                ar[val]+=op
                val += val & -val

        arr = [0 for i in range(max(rating)+2)]
        arr2 = [0 for i in range(max(rating)+2)]
        arr3 = [0 for i in range(max(rating)+2)]
        arr4= [0 for i in range(max(rating)+2)]
        for i in rating:
            l,r = query(i,arr)
            arr2[i]= l
            arr3[i] = r
            update(i,1,arr)
        count = 0
        for i in range(len(rating)-1,-1,-1):
            val = rating[i]
            l ,r =  query(val,arr4)
            count += l *arr3[val]
            count += r * arr2[val]
            update(val,1,arr4)
        return count