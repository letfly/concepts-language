# http://oj.leetcode.com/problems/search-for-a-range/
class Solution(object):
    def search_range(self, nums, target):
        #
        first = 0
        last = len(nums)
        if nums[last-1]>=target>=nums[0]:
            while first < last:
                medium = (first+last)/2
                if nums[medium] > target:
                    last = medium
                elif nums[medium] < target:
                    first = medium
                else:
                    start = end = medium
                    while start > 0 and nums[start - 1] == target:
                        start -= 1
                    while end + 1 < len(nums) and nums[end + 1] == target:
                        end += 1
                    return [start, end]
        return [-1, -1]

s = Solution()
print s.search_range([5, 7, 7, 8, 8, 8, 10], 8)
