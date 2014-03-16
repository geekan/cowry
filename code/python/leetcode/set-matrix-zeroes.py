class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        nrow = len(matrix)
        ncolumn = len(matrix[0])
        row_zeros = False
        column_zeros = False
        for row in range(nrow):
            for column in range(ncolumn):
                if matrix[row][column] == 0:
                    matrix[row][0] = matrix[0][column] = 0
                    if row == 0:
                        row_zeros = True
                    if column == 0:
                        column_zeros = True

        for row in range(1, nrow):
            if matrix[row][0] == 0:
                for i in range(ncolumn):
                    matrix[row][i] = 0
        for column in range(1, ncolumn):
            if matrix[0][column] == 0:
                for i in range(1, nrow):
                    matrix[i][column] = 0

        if row_zeros:
            for i in range(ncolumn):
                matrix[0][i] = 0
        if column_zeros:
            for i in range(nrow):
                matrix[i][0] = 0

matrix = [
  [1, 3, 5, 7],
  [0, 1, 0, 2],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]
Solution().setZeroes(matrix)
for i in matrix:
    print i