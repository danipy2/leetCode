class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            if r - l <= 1:
                return
            mid = (l + r) // 2
            mergeSort(l, mid)
            mergeSort(mid, r)
            temp = []
            i, j = l, mid
            while i < mid and j < r:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            temp.extend(nums[i:mid])
            temp.extend(nums[j:r])
            nums[l:r] = temp
        mergeSort(0, len(nums))
        return nums