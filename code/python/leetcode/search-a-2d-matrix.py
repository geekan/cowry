class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def search_row(self, row, target):
        if target in row:
            return True
        return False

    def searchMatrix(self, matrix, target):
        n = len(matrix)
        for row_index in range(n):
            if matrix[row_index][0] > target and row_index > 0:
                return self.search_row(matrix[row_index-1], target)
        if matrix[row_index][-1] >= target:
            return self.search_row(matrix[row_index], target)
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print Solution().searchMatrix(matrix, 50)