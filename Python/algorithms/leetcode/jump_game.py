class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, n in enumerate(nums):
            print i,n
            if i > m:
                return False
            m = max(m, i+n)
        return True

s = Solution()
print s.canJump([2,3,1,1,4])
