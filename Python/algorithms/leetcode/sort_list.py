# https://leetcode.com/problems/sort-list/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next
    def sort_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sort_list, (head, slow)))

s = Solution()
l = [5, 7, 7, 8, 8, 8, 3]
for i in xrange(len(l) - 1):
    node = ListNode(l[i])
    node.next = ListNode(l[i+1])
print s.sort_list(node).val
