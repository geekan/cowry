# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if p == None and q == None:
        return True
    elif p == None or q == None:
        return False
    elif p.left == None and p.right == None and q.left == None and q.right == None:
        return p.val == q.val
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right) and p.val == q.val
    return False

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        return is_same_tree(p, q)

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

print Solution().isSameTree(p, q)