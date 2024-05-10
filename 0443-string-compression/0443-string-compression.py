class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        count = 0
        for i in range(len(chars)):
            if chars[i] != chars[left]:
                if i-left-1:
                    chars[count] = chars[left]
                    count += 1
                    for char in(str(i-left)):
                        chars[count]= char
                        count+=1
                else:
                    chars[count] = chars[left]
                    count+=1
                left = i
        if len(chars)-left-1:
            chars[count]=chars[left]
            count+=1
            for char in(str(len(chars)-left)):
                chars[count]=(char)
                count += 1
        else:
            chars[count] = chars[left]
            count+=1
        return count     


        