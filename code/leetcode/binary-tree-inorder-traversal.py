# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.l = []

    def inorderTraversal(self, root):
        if root is None:
            return []
        #print root.val
        self.inorderTraversal(root.left)
        self.l.append(root.val)
        self.inorderTraversal(root.right)
        return self.l

p = TreeNode(1)
pr1 = TreeNode(2)
pl2 = TreeNode(4)
pr3 = TreeNode(3)
p.left = pr1
pr1.left = pl2
pl2.right = pr3

q = TreeNode(1)
qr1 = TreeNode(4)
ql2 = TreeNode(2)
qr3 = TreeNode(3)
q.left = qr1
qr1.left = ql2
ql2.right = qr3

print Solution().inorderTraversal(p)