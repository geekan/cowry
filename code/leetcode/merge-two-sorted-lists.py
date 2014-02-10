# Definition for singly-linked list.
class ListNodeX:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        
        n1 = l1
        n2 = l2
        nh = ListNodeX(0)
        nn = nh

        while n1 and n2:
            if n1.val < n2.val:
                nn.next = n1
                n1 = n1.next
            else:
                nn.next = n2
                n2 = n2.next
            
            if nn.next is not None:
                nn = nn.next

        if n1:
            nn.next = n1
        else:
            nn.next = n2
        return nh.next

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

x1 = [-10,-10,-9,-4,1,6,6]
x2 = [-7]

o1 = genr_list(x1)
o2 = genr_list(x2)

new = Solution().mergeTwoLists(o1, o2)

print show_list(new)
