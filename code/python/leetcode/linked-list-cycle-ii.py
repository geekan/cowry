# 朴素思想1：
# 如果想要空间上O(1) (原来是O(n)
# 可以先遍历一遍，看是否有linked
# 然后折半查找linked的点
# 时间复杂度由O(n)变为O(nlgn)
#
# 进阶思想2：
# 见龟兔问题
# http://blog.csdn.net/sysucph/article/details/15378043

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
arr = [1,2,3,4,5]
r = build_list(arr)
print Solution().detectCycle(r)
r.next.next = r
print Solution().detectCycle(r)