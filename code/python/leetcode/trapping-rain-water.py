# 2-pass solution.
# note the A[i] >= expected..
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        expected = 0
        eindex = 0
        rain = 0
        block = 0
        for i in range(len(A)):
            if A[i] >= expected:
                rain += (i-eindex-1)*expected - block
                block = 0
                expected = A[i]
                eindex = i
            else:
                block += A[i]

        expected = eindex = block = 0
        for i in range(len(A)-1, -1, -1):
            if A[i] > expected:
                rain += (eindex-i-1)*expected - block
                block = 0
                expected = A[i]
                eindex = i
            else:
                block += A[i]
        return rain

A = [0,1,0,2,1,0,1,3,2,1,2,1] # 1+1+2+1 = 5
print Solution().trap(A)