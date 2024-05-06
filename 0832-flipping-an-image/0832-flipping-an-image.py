class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            right = len(i)-1
            left = 0
            while(left<=right):
                tempo = i[right]
                if i[left]:
                    i[right] = 0
                else:
                    i[right] = 1
                if tempo:
                    i[left]= 0
                else:
                    i[left]= 1
                left+=1
                right-=1
        return image
                
