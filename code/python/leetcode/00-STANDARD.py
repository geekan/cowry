
def genr_list(xlist):
    old = lh = ListNodeX(0)
    for i in xlist:
        lnode = ListNodeX(i)
        old.next = lnode
        old = lnode
    return lh.next

def show_list(lnode):
    l = []
    while lnode:
        l.append(lnode.val)
        lnode = lnode.next
    return l

def build_tree(intlist):
    length = len(intlist)
    llist = [TreeNode(i) for i in intlist]
    for i in range(length):
        llist[i].left = llist[i*2+1] if length > i*2+1 and intlist[i*2+1] != '#' else None
        llist[i].right = llist[i*2+2] if length > i*2+2 and intlist[i*2+2] != '#' else None
    print llist
    return llist

# Definition for singly-linked list.
class ListNodeX:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        #self.next = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    max_layer = 0
    min_layer = 999
    
    def traversal(self, root, layer):
        if root is None:
            self.max_layer = max(self.max_layer, layer)
            self.min_layer = min(self.min_layer, layer)
            return
        self.traversal(root.left, layer + 1)
        self.traversal(root.right, layer + 1)
    
    def isBalanced(self, root):
        self.traversal(root, 0)
        print self.max_layer, self.min_layer
        return True if self.max_layer - self.min_layer <= 1 else False

#r = [TreeNode(x) for x in range(10)]
r = build_tree([1,2,2,3,3,3,3,4,4,4,4,4,4,'#','#',5,5])

print Solution().isBalanced(r[0])