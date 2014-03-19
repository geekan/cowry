class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        cur = [root]
        depth = 1
        while cur:
            next = []
            for node in cur:
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
                if node.left == None and node.right == None:
                    return depth
            cur = next
            depth += 1

root = build_tree([1,2,2,3,3,3,'#'])
print Solution().minDepth(root)