class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        res = []
        for num in arr2:
            res += [num] * count.pop(num, 0)
        rest = sorted(count.keys())
        for num in rest:
            res += [num] * count[num]
        return res
