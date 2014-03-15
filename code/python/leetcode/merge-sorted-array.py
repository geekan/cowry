class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        for i in range(n):
            A[m] = B[i]
            m += 1
        A.sort()

A = [1,2,3,0,0,0]
B = [4,5,6]

Solution().merge(A, 3, B, len(B))
print A

A = [0]
B = [1]
Solution().merge(A, 0, B, len(B))
print A

A = [1]
B = [0]
Solution().merge(A, 1, B, 0)
print A

A = [1, 0]
B = [2]
Solution().merge(A, 1, B, len(B))
print A