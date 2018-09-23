
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0

        def oneMaxProfit(prices):
            profit=0
            low=prices[0],0
            tep_low=prices[0],0
            high=0
            for i in range(len(prices)):
                if prices[i]<tep_low[0]:
                    tep_low=prices[i],i

                if prices[i]-tep_low[0]>profit:
                    profit=prices[i]-tep_low[0]
                    low=tep_low
                    high=i

            return profit,low[1],high
        n=len(prices)
        profit,i,j=oneMaxProfit(prices)
        if profit==0:
            return 0
        elif i==0 and j==n-1:
            p1= profit
        elif i==0:
            p1=profit+oneMaxProfit(prices[j+1:])[0]
        elif j==n-1:
            p1=profit+oneMaxProfit(prices[:i])[0]
        else:
            p1=profit+max(oneMaxProfit(prices[j+1:])[0],oneMaxProfit(prices[:i])[0])

        reversed_ls=list(reversed(prices[i:j]))
        m,x,y=oneMaxProfit(reversed_ls)
        print(m,x,y)

        p2=prices[j]-reversed_ls[x]+reversed_ls[y]-prices[i]
        return max(p1,p2)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1=buy2=float("-inf")
        sell1 = sell2 = 0
        for i in range(len(prices)):
            sell1 = max(sell1,prices[i]+buy1)
            buy1 = max(buy1,-prices[i])
            sell2 = max(sell2,prices[i]+buy2)
            buy2 = max(buy2,sell1-prices[i])
        return max(sell1,sell2)
solution=Solution()
p=[1,4,2,7]
print(list(reversed(p)))


print(solution.maxProfit(p))