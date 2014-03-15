class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        #self.next = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        cur = [root]
        while cur:
            all_none = True
            next = []
            for x in cur:
                if x is None:
                    continue
                all_none = False
                next.append(x.left)
                next.append(x.right)
            for i in range(len(cur)/2):
                if cur[i] == None or cur[-1-i] == None:
                    if cur[i] == cur[-1-i]:
                        continue
                    else:
                        return False
                elif cur[i].val != cur[-1-i].val:
                    return False
            if all_none == True:
                break
            cur = next
        return True

r = [TreeNode(x) for x in range(10)]
r[0].left = r[1]
r[0].right = r[2]
r[1].val = 2
r[1].left = r[3]
r[1].right = r[4]
r[2].left = r[5]
r[5].val = 4
r[2].right = r[6]
r[6].val = 3

print Solution().isSymmetric(r[0])