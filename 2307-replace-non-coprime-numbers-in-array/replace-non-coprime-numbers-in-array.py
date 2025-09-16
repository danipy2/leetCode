class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in nums:
            num = i 
            
            cond = True
            while ans and cond:
                cond  = math.gcd(num,ans[-1])!=1
                if cond:
                    num = math.lcm(num,ans[-1])
                    ans.pop()
                        
                
            ans.append(num)

        return ans