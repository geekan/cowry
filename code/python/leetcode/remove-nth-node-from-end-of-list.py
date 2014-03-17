class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        slow = fast = head
        # first loop, move fast ahead of slow n steps
        # if len(head) == n, then return head.next
        for i in range(n):
            fast = fast.next
            if not fast:
                return head.next
        while fast:
            for i in range(n):
                fast = fast.next
                if not fast:
                    break
                slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        return head

head = build_list([1,2,3,4,5,6])
print show_list(Solution().removeNthFromEnd(head, 1))