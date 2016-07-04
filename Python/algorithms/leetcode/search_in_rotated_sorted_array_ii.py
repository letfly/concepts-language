class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        f, l = 0, len(nums)-1
        while f <= l:
            mid = f + (l-f)//2
            if nums[mid] == target:
                return True
            while f < mid and nums[f] == nums[mid]: # tricky part
                f += 1
            # the first half is ordered
            if nums[f] <= nums[mid]:
                # target is in the first half
                if nums[f] <= target < nums[mid]:
                    l = mid - 1
                else:
                    f = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[f]:
                    f = mid + 1
                else:
                    l = mid - 1
        return False

s = Solution()
print s.search([1,5,4,4,5,7,4], 4)
