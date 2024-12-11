'''
Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
'''

class Solution:
    def maximumProfit(self, prices):
        # code here
        bp = prices[0]
        mp=0
        for p in prices:
            if p>bp:
                mp = max(mp,p-bp)
            bp = min(bp,p)
        return mp
                
