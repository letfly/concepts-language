# https://oj.leetcode.com/problems/sqrtx/
class Solution(object):
    def my_sqrt(self, x):
        """
        :type x: integer
        :rtype: integer
        """
        # find the mid*mid == x
        f, l = 0, x
        while f <= l:
            mid = (f+l)/2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                l = mid - 1
            else:
                f = mid + 1

s = Solution()
print s.my_sqrt(0)
