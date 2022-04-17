from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left_pointer,right_pointer = 0, len(matrix)-1
        while left_pointer < right_pointer:
            for i in range(right_pointer - left_pointer):
                top,down = left_pointer,right_pointer
                temp = matrix[top][left_pointer+i]
                matrix[top][left_pointer+i] = matrix[down - i][left_pointer]
                matrix[down - i][left_pointer] = matrix[down][right_pointer - i]
                matrix[down][right_pointer - i] = matrix[top + i][right_pointer]
                matrix[top + i][right_pointer] = temp
            left_pointer+=1
            right_pointer-=1