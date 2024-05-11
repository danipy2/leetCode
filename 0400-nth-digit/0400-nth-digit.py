class Solution:
    def findNthDigit(self, n: int) -> int:
        x= 9
        num = n
        count = 0
        while (n-x>0):
            num = n
            count += 1
            num -= x
            x += (10**count) *( 9 * (count+1))
        count += 1
        digit = count+1 -((num) % (count))
        
        if digit > count:
            digit = 1
        num2 = 10**(count-1) + (num-1)//count   
        return  int(str(num2)[count-digit])
            

            

        