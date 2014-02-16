 class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        ml = self.maxDepth(root.left) + 1
        mr = self.maxDepth(root.right) + 1
        return ml if ml > mr else mr