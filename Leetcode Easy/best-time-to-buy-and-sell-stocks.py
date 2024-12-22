
def maxProfit(self, prices):
        
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):
            currentPrice = prices[i]
        
            if minPrice>currentPrice:
                minPrice= currentPrice
        
            potentialProfit = currentPrice-minPrice

            if potentialProfit>maxProfit:
                maxProfit = potentialProfit
            
        return maxProfit