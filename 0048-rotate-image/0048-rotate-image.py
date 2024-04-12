class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        list2 = []
        for i in range(len(matrix)):
            list1 = []
            for j in range(len(matrix)-1,-1,-1):
                list1.append(matrix[j][i])
            list2.append(list1)
        for i in range(len(matrix)):
            matrix[i] = list2[i]




        