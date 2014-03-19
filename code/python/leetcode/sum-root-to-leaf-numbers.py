class Solution:
    # @param root, a tree node
    # @return an integer
    
    def recr(self, root, x):
        if root is None:
            return
        x = x*10 + root.val
        if root.left == root.right == None:
            self.sum += x
            return
        self.recr(root.left, x)
        self.recr(root.right, x)

    def sumNumbers(self, root):
        self.sum = 0
        self.recr(root, 0)
        return self.sum

root = build_tree([1,2,2,3,3,'#',3])
print Solution().sumNumbers(root)
