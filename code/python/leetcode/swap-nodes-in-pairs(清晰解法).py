class Solution:
    # @param a ListNode
    # @return a ListNode
    
    def swap(self, prev, next):
        prev.next = next.next
        next.next = prev
        return next

    def swapPairs(self, head):
        if not head or head.next is None:
            return head
        lh = ListNode(0)
        lh.next = head
        p = lh
        while p.next and p.next.next:
            p.next = self.swap(p.next, p.next.next)
            p = p.next.next
        return lh.next