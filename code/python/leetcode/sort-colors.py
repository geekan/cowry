class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    
    def swap(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp
        return
    
    def partition(self, A, start, end):
        if start > end:
            return
        pivot_value = A[start]
        store_index = start
        self.swap(A, start, end) # swap pivot to end (restore)

        for i in range(start, end):
            if pivot_value > A[i]:
                self.swap(A, i, store_index)
                store_index += 1

        self.swap(A, store_index, end) # swap pivot to store_index
        self.partition(A, start, store_index-1)
        self.partition(A, store_index+1, end)

    def quick_sort(self, A, start, end):
        self.partition(A, start, end)
    
    def sortColors(self, A):
        self.quick_sort(A, 0, len(A)-1)

A = [1,5,10,2,9,4]
Solution().sortColors(A)
print A