
# Best time to buy and sell stock 2.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# FIXME, add a cache memory call (maybe ?).
def maxProfit(prices: list[int]) -> int:

    # debug.
    #print(f'T: {prices}')

    # cut if array to short to buy and sell.
    if len(prices) <= 1:
        return 0
    
    # when only one possibility buy-sell.
    if len(prices) == 2:
        return max(prices[1] - prices[0], 0)
    
    # skip first (if bigest).
    is_bigest_val = max(prices) == prices[0]
    if is_bigest_val:
        prices.pop(0)
        return maxProfit(prices)  # recurse (legit), skip first if every next sell is a negatif profit.
    
    all_benef = [ (k, prices[k]-prices[0]) for k in range(1, len(prices)) if prices[k]-prices[0] > 0 ]
    #all_benef.sort(key=lambda e: e[1], reverse=True)
    best_way = -1
    for ab in all_benef:
        current_benef = ab[1] + maxProfit(prices[ab[0]+1:])  # recurs (maybe can be reduced, FIXME), calcul rest of other days, for all case.
        if current_benef > best_way:
            best_way = current_benef
    
    return max(best_way, maxProfit(prices[1:]))  # recurs, can be more profit to skip first buy.



print(maxProfit([7,1,5,3,6,4]))  # 7.
# buy for 1.
# sell for 5 (--> 4 benef).
# buy for 3.
# sell for 6 (--> 3 benef).
# total benef = 4+3 -> 7.
print(maxProfit([1,2,3,4,5]))  # 4.
print(maxProfit([7,6,4,3,1]))  # 0.
