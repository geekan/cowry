class Solution:
    # @param root, a tree node
    # @return a boolean
    
    def traversal(self, root):
        if root is None:
            return 1
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        if left is False or right is False:
            return False
        left_depth = 1 + left
        right_depth = 1 + right
        if abs(left_depth-right_depth) > 1:
            return False
        return max(left_depth, right_depth)

    def isBalanced(self, root):
        if self.traversal(root) == False:
            return False
        else:
            return True