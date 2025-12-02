"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
Category: Two pointers
"""

prices = [7,1,5,3,6,4]

def maxProfit(prices):
    maxProfit = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l += 1
        r += 1
    return maxProfit