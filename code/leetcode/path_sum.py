# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sum_(root, s, sum):
    if root is None:
        return
    s += root.val

    if root.left == None and root.right == None and s == sum:
        return True
    if sum_(root.left, s, sum) or sum_(root.right, s, sum):
        return True

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if sum_(root, 0, sum):
            return True
        else:
            return False

s = Solution()
root = TreeNode(-3)
l1 = TreeNode(-9)
l2 = TreeNode(-5)
l1.left = l2
l3 = TreeNode(7)
l2.left = l3
l4 = TreeNode(2)
l3.left = l4

#r1 = TreeNode(12)
root.left = l1
#root.right = r1
print s.hasPathSum(root, -8)
