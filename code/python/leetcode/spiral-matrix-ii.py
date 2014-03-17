class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = [[0 for i in range(n)] for j in range(n)]

        curn = 0
        m = n
        while m > 0:
            for i in range(n-m, m):
                matrix[n-m][i] = curn + 1
                curn += 1

            for i in range(n-m+1, m):
                matrix[i][m-1] = curn + 1
                curn += 1

            for i in range(m-2, n-m-1, -1):
                matrix[m-1][i] = curn + 1
                curn += 1
            
            for i in range(m-2, n-m, -1):
                matrix[i][n-m] = curn + 1
                curn += 1

            m -= 1
        return matrix

m1 = [
      [1,2,3,4],
      [1,2,3,5],
      [1,2,3,6],
      [1,2,3,7],
]

for i in Solution().generateMatrix(3):
    print i
