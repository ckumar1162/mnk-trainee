# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def profit(price):
    max_profit = 0
    min_price = float('inf')
    print(min_price)
    for i in price:
        min_price = min(min_price,i)
        profit = i-min_price
        max_profit = max(profit,max_profit)
    return max_profit

print(profit([7,1,5,3,6,4]))
print(profit([7,6,4,3,1])) 
print(profit([7,2,4,9,1,3])) 
    