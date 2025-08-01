prices=list(map(int, input().split()))
profit = 0
i = 0
#while i < len(prices) - 1:
 #if prices[i] < prices[i + 1]:
    #profit += prices[i + 1] - prices[i]
 #i += 1
#print(profit)
for i in range(len(prices)-1):
    if prices[i]<prices[i+1]:
        profit +=prices[i+1]-prices[i]
print(profit)