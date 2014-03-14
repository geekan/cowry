class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        uindex = 0
        for i in range(1, len(A)):
            if A[uindex] == A[i]:
                continue
            else:
                uindex += 1
                A[uindex] = A[i]
        return uindex + 1

A = [1,1,2,2,2,3,3]
print Solution().removeDuplicates(A)
print A