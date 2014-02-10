class Solution:
    def __init__(self):
        self.l = []

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        self.l.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.l