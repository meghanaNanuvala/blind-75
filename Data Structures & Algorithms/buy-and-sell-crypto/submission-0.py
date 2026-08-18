class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]
        

        for price in prices:
            if price < buy:
                buy = price
            else:
                maxP = max(maxP, price - buy)

        return maxP




        

        