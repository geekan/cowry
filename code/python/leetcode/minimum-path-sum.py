    class Solution:
        # @param grid, a list of lists of integers
        # @return an integer
        def minPathSum(self, grid):
            m = len(grid)
            n = len(grid[0])
            for i in range(m):
                for j in range(n):
                    if i == j == 0:
                        pass
                    elif i == 0:
                        grid[i][j] += grid[i][j-1]
                    elif j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            return grid[-1][-1]
grid = [
    [1,1,1,1,2],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
print Solution().minPathSum(grid)