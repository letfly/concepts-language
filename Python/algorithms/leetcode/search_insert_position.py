class Solution(object):
    def searchInsert(self, nums, key):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if key > nums[len(nums) - 1]:
            return len(nums)

        if key < nums[0]:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)/2
            print m
            if nums[m] > key:
                r = m - 1
                if r >= 0:
                    if nums[r] < key:
                        return r + 1
                else:
                    return 0

            elif nums[m] < key:
                l = m + 1
                if l < len(nums):
                    if nums[l] > key:
                        return l
                else:
                    return len(nums)
            else:
                return m

s = Solution()
print s.searchInsert([1,3,5,7], 2)
