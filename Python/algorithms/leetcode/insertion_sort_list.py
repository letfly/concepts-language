# https://leetcode.com/problems/insertion-sort-list/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            n_val = cur.next.val;print n_val,p.val,p.next.val
            if cur.val < n_val:
                cur = cur.next
                continue
            if p.next.val > n_val:
                p = dummy
            while p.next.val < n_val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next

s = Solution()
l = [5, 7, 7, 8, 8, 8, 3]
for i in xrange(len(l) - 1):
    while node.next is not None:
        node = node.next
    node.next = ListNode(l[i+1])
while node:
    print node.val
    node = node.next
s.insertionSortList(node)
