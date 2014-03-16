class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers

    def swap_2d(self, arr, x, y, n):
        arr[y][x], arr[x][n-y] = arr[x][n-y], arr[y][x]
        arr[y][x], arr[n-y][n-x] = arr[n-y][n-x], arr[y][x]
        arr[y][x], arr[n-x][y] = arr[n-x][y], arr[y][x]

    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n/2 + n%2):
            for j in range(n/2):
                self.swap_2d(matrix, i, j, n-1)
        return matrix

matrix = [
          [1,2,3],
          [4,5,6],
          [7,8,9],
]

m1 = Solution().rotate(matrix)
for x in m1:
    print x

matrix = [
          [1,2],
          [3,4]
]
m1 = Solution().rotate(matrix)
for x in m1:
    print x