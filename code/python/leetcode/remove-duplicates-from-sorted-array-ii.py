class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        record = A[0]
        dup = count = i = 1
        while i < len(A):
            if A[i] == record:
                dup += 1
            else:
                dup = 1
                record = A[i]

            if dup >= 3:
                del A[i]
            else:
                i += 1
                count += 1
        return count

A = [1,1,1,1,1,2,2,2,3,4,4,4,4]
print Solution().removeDuplicates(A)
print A
