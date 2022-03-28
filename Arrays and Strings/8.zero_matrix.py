from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_col_zero = False

        # use 0th row and 0th column as flag to indicate column and row should be 0 or not

        for i in range(m):
            # while iterating through all the rows,check if any of cell in the 0th column is 0
            # if any cell is 0,we need to update 0th columns as well
            if matrix[i][0] == 0:
                first_col_zero = True

            # check all cells starting from column 1,
            # if any cell is 0,add flag (in 0th row and 0th col)
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # at this point,matrix has updated with flag row and col
        # iterate through 1st row and 1st column and if check for flag to update the row
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # finally update 0th row and 0th col

        # if (0,0) cell is 0,update 0th row
        # ( we tracked any 0th column value is 0 by first_col_zero variable)
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0

        # if first_col_zero is true means,originally 0th column had 0 cell
        # so update the entire column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        print(matrix)