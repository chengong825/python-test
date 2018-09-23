prices=[7,1,5,3,6,4]
prices=[1,5,2,8,0,3,6]
def maxProfit(prices):
    n=len(prices)
    i=0
    minprice=prices[0]
    profit=0
    while i<n:
        if prices[i]<minprice:
            minprice=prices[i]
        if profit<prices[i]-minprice:
            profit=prices[i]-minprice
        i+=1
    return profit
print(maxProfit(prices))
