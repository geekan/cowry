class Solution:
    # @param root, a tree node
    # @return a list of integers
    def pt(self, root):
        if root is None:
            return
        self.pt(root.left)
        self.pt(root.right)
        self.ints.append(root.val)
    
    def postorderTraversal(self, root):
        self.ints = []
        self.pt(root)
        return self.ints

arr = [1,2,2,3,3,3,3]
root = build_tree(arr)
print Solution().postorderTraversal(root)