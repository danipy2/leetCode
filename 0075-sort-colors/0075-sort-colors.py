class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[0,0,0]
        for i in nums:
            if i == 0:
                arr[0] += 1
            elif i == 1:
                arr[1] +=1
            else:
                arr[2] +=1
        index = 0
        while(arr[0]>0):
            nums[index]= 0
            arr[0] -=1
            index+=1
        
        while(arr[1]>0):
            nums[index]=1
            index += 1
            arr[1] -=1
        while(arr[2]>0):
            nums[index] = 2
            index += 1
            arr[2] -=1

            

        