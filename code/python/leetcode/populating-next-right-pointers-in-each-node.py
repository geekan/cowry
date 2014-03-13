class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        cur = [root]
        while cur:
            next = []
            lenroot = len(cur)
            for i in range(lenroot):
                # print x.val
                if i != lenroot - 1:
                    cur[i].next = cur[i + 1]
                if cur[i].left: next.append(cur[i].left)
                if cur[i].right: next.append(cur[i].right)
            cur = next

r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r1.left = r2
r1.right = r3
r4 = TreeNode(4)
r5 = TreeNode(5)
r2.left = r4
r2.right = r5
r6 = TreeNode(6)
r7 = TreeNode(7)
r3.left = r6
r3.right = r7

s = Solution()
s.connect(r1)