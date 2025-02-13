class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        count_odd =0
        l = 0
        myset = []
        for i in range(len(nums)):
            if nums[i]%2:
                myset.append(i)
                count_odd+=1
            if count_odd >k:
                if l:
                    l1 = (myset[l]-(myset[l-1]))
                    r = i-myset[-2]
                    total += l1*r
                else:
                    r = i-myset[-2]
                    total += (myset[l]+1)*r
                l+=1
                count_odd-=1
                print(total,i)
        if count_odd >=k:
            if l:
                l1 = (myset[l]-(myset[l-1]))
                r = (len(nums)-myset[-1])
                total += l1*r
                print(total,l,r,myset)
            else:
                r = (len(nums)-myset[-1])
                total += (myset[l]+1)*r
            print(total)
        return total