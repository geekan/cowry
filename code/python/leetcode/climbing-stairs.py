class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n in range(3):
            return n
        fib = [1, 2]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n - 1]

print Solution().climbStairs(5)