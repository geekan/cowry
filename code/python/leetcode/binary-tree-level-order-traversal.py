class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        cur = [root]
        ints = []
        while cur:
            ints.append([x.val for x in cur])
            next = []
            for i in cur:
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            cur = next
        return ints

arr = [1,2,2,3,3,'#',3]
root = build_tree(arr)
print Solution().levelOrder(root)