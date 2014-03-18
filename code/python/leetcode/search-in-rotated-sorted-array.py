# NEED REVIEW
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        l = 0
        r = len(A)-1
        while l <= r:
            mid = (l+r)/2
            if A[mid] == target:
                return mid
            if A[l] <= A[mid]: # ordered left
                if A[mid] > target and A[l] <= target:
                    r = mid-1
                else:
                    l = mid+1
            else: # ordered right
                if A[mid] < target and A[r] >= target:
                    l = mid+1
                else:
                    r = mid-1
        return -1

A = [4,5,6,7,8,9,0,1,2,3]
print Solution().search(A, 0)