class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(0, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit

s = Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
