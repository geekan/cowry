class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A is None:
            return 0
        
        for index, i in enumerate(A):
            if i >= target:
                return index
        return index + 1

target = 8
A = [1,3,5,7]

print Solution().searchInsert(A, target)