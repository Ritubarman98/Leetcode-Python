prices=list(map(int, input().split()))
min_price=float('inf')
profit=0

for price in prices:
    min_price=min(min_price, price)
    profit= max(profit, price-min_price)
print(profit)  