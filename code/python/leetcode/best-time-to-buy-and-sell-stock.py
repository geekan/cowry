class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        max = min = prices[0]
        mdiff = 0
        for p in prices:
            if p > max: max = p
            if p < min:
                min = p
                max = p
            if max - min > mdiff: mdiff = max - min
        return mdiff
print Solution().maxProfit([1,3,5,9,3,7,4,1])
print Solution().maxProfit([2,1])