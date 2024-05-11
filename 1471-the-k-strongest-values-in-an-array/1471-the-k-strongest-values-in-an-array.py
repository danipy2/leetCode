class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        count = 0
        left = 0
        right = len(arr)-1
        mid = arr[right//2]
        output = []
        while(count<k):
            right1 = abs(arr[right]-mid)
            left1 =abs(arr[left]-mid)
            if right1 >= left1 :
                output.append(arr[right])
                right -=1
                count+=1
            else:
                output.append(arr[left])
                left +=1
                count+=1
        return output

        