# https://oj.leetcode.com/problems/remove-element/
class Solution(object):
    def remove_element(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = filter(lambda x: x!= val, nums)
        return len(nums)

s = Solution()
print s.remove_element([3,2,2,3], 3)
