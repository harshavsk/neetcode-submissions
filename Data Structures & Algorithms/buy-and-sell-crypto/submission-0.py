class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        r =len(prices)-1
        for l,price in enumerate(prices):
            i = l+1
            while i<=r:
                if price<prices[i]:
                    maxProfit= max(maxProfit, prices[i]-price)
                i+=1
        return maxProfit     