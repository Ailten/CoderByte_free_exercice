
# best time to buy and sell stock.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices: list[int]) -> int:

    max_profit: int|None = None

    for i in range(len(prices)-1):
        price_buy = prices[i]
        for j in range(i+1, len(prices)):
            price_sell = prices[j]
            profit = price_sell - price_buy
            if profit >= (max_profit or profit):
                max_profit = profit

    if max_profit == None or max_profit <= 0:
        return 0
    return max_profit


print(maxProfit([7,1,5,3,6,4]))  # 5.
print(maxProfit([7,6,4,3,1]))  # 0.  -> no transaction, so return 0.