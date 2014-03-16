class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def bfs(self, root):
        cur = [root]
        vals = []
        while cur:
            next = []
            cur_vals = []
            vals.append([x.val for x in cur])
            for i in cur:
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            cur = next
        return vals

    def levelOrderBottom(self, root):
        return [x for x in reversed(self.bfs(root))] if root else []

root = build_tree([1,2,'#',3,3,3,3])[0]
print root
print Solution().levelOrderBottom(root)