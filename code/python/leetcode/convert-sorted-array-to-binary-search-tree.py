class Solution:
    # @param num, a list of integers
    # @return a tree node
    def build_bst(self, arr, start, end):
        if start > end:
            return None
        mid = (start+end)/2
        root = TreeNode(arr[mid])
        root.left = self.build_bst(arr, start, mid-1)
        root.right = self.build_bst(arr, mid+1, end)
        return root
        
    def sortedArrayToBST(self, num):
        return self.build_bst(num, 0, len(num)-1)

arr = [1,3,4,5,6,7,8,9,10]

# 1884
s = [1, 90, 99, 3999]
root = Solution().sortedArrayToBST(arr)
print root