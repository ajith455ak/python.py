prices =eval(input("enter the price "))
first_buy = min(float('inf'), prices[0])
first_profit = 0
second_buy = min(float('inf'), prices[0])
second_profit = 0
for price in prices[1:]:
    first_buy = min(first_buy, price)
    first_profit = max(first_profit, price - first_buy)
    second_buy = min(second_buy, price - first_profit)
    second_profit = max(second_profit, price - second_buy)
print(second_profit)
