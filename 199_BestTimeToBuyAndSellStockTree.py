
# best time to buy and sell stock 3
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


def maxProfit(prices: list[int]) -> int:

    def bestSell(arr_prices: list[int]) -> int:
        best_benef = -1
        for i in range(len(arr_prices)-1):
            buy = arr_prices[i]
            for j in range(i+1, len(arr_prices)):
                sell = arr_prices[j]
                if sell < buy:
                    continue
                benef = sell - buy
                if benef > best_benef:
                    best_benef = benef
        return best_benef if best_benef > 0 else 0

    paths = []

    best_benef_many = bestSell(prices)  # check the full range (one transaction).
    for i_split in range(2, len(prices)-1):
        current_benef = (
            bestSell(prices[:i_split]) + 
            bestSell(prices[i_split:])
        )
        if current_benef > best_benef_many:
            best_benef_many = current_benef
    return best_benef_many if best_benef_many > 0 else 0


print(maxProfit([3,3,5,0,0,3,1,4]))  # 6.
print(maxProfit([1,2,3,4,5]))  # 4.
print(maxProfit([7,6,4,3,1]))  # 0.