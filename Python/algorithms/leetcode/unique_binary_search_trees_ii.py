# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            print val, left, right
            return node
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        if n<1:
            return []
        return trees(1, n)

s = Solution()
print s.generateTrees(3)
