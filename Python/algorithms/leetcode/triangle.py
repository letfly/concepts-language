class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                print res
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]

s = Solution()
print s.minimumTotal([[2],[3,4],[6,5,7],[4,3,8,1]])
