# 对于任意一点(x,y)都可以从(x-1,y)+(x,y-1)走到
# 由此做DP
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        arr = [[1 for x in range(n)] for y in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # print i,j
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
                # print arr
        return arr[-1][-1]

print Solution().uniquePaths(3, 7)