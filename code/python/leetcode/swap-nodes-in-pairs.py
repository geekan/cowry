class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or head.next is None:
            return head
        new_head = head.next
        ptr1 = head
        ptr2 = head.next
        while ptr2:
            ptr1.next = ptr2.next.next if ptr2.next and ptr2.next.next else ptr2.next
            next = ptr2.next
            ptr2.next = ptr1
            ptr1 = next
            ptr2 = next.next if next else None
        return new_head

l = genr_list([1,2,3,4,5,6,7,8,9,10])
ls = Solution().swapPairs(l)
print show_list(ls)