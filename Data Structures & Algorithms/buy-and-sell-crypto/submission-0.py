class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        maxp = 0
        while buy<len(prices):
            while sell<len(prices):
                p = prices[sell]-prices[buy]
                if p>maxp:
                    maxp = p
                sell+=1
            buy+=1
            sell=buy+1
        return maxp 